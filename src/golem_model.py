"""Equal-variance GOLEM and a one-hot, group-lasso Gaussian surrogate.

W[source, target]; X_hat = X @ W. The categorical extension penalizes DAGs
at the original-variable level, not at the dummy-column level.
"""
from dataclasses import asdict, dataclass

import networkx as nx
import numpy as np
import torch
from causallearn.graph.GraphNode import GraphNode

from constraints import build_background_knowledge


@dataclass(frozen=True)
class FitConfig:
    lambda1: float = 0.02
    lambda_dag: float = 5.0
    learning_rate: float = 0.001
    max_iter: int = 10000
    tolerance: float = 1e-7
    check_every: int = 100
    patience: int = 5
    seed: int = 0

    def validate(self):
        if not all(np.isfinite(v) and v >= 0 for v in
                   (self.lambda1, self.lambda_dag, self.tolerance)):
            raise ValueError("Penalties and tolerance must be finite and nonnegative")
        if not np.isfinite(self.learning_rate) or self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if min(self.max_iter, self.check_every, self.patience) < 1:
            raise ValueError("Iteration settings must be positive")


def vocabulary(df, names):
    return {n: sorted(df[n].unique().tolist()) for n in names}


def prepare(df, names, representation, categories=None):
    if not len(df) or df[names].isna().any().any():
        raise ValueError("Empty data or missing values")
    if any(df[n].nunique() < 2 for n in names):
        raise ValueError("A model variable is constant")
    if representation == "continuous":
        x = df[names].to_numpy(dtype=float)
        sizes = [1] * len(names)
        scale = x.std(axis=0)
    elif representation == "discretized":
        categories = categories or vocabulary(df, names)
        if any(not df[n].isin(categories[n]).all() for n in names):
            raise ValueError("Unknown category")
        sizes = [len(categories[n]) for n in names]
        x = np.concatenate([(df[n].to_numpy()[:, None] == categories[n]).astype(float)
                            for n in names], axis=1)
        scale = np.ones(x.shape[1])
    else:
        raise ValueError(f"Unknown representation: {representation}")
    mean = x.mean(axis=0)
    x = (x - mean) / scale
    if not np.isfinite(x).all():
        raise ValueError("Nonfinite model input")
    return x, sizes, {"mean": mean.tolist(), "scale": scale.tolist(),
                      "categories": categories, "group_sizes": sizes}


def allowed_mask(names, constrained, size_vars=None):
    mask = np.ones((len(names), len(names))) - np.eye(len(names))
    if constrained:
        bk = build_background_knowledge(names, size_vars=size_vars)
        for i, a in enumerate(names):
            for j, b in enumerate(names):
                if bk.is_forbidden(GraphNode(a), GraphNode(b)):
                    mask[i, j] = 0
    return mask


def block_indices(sizes):
    offsets = np.cumsum([0] + sizes)
    width = max(sizes) ** 2
    d = sum(sizes)
    indices = np.full((len(sizes), len(sizes), width), d * d, dtype=int)
    for i in range(len(sizes)):
        for j in range(len(sizes)):
            ix = [a * d + b for a in range(offsets[i], offsets[i + 1])
                  for b in range(offsets[j], offsets[j + 1])]
            indices[i, j, :len(ix)] = ix
    return torch.tensor(indices, dtype=torch.long)


def objective(w, covariance, indices, config):
    """Batched exact centered-data objective using sufficient statistics."""
    d = w.shape[-1]
    residual = torch.eye(d, dtype=w.dtype) - w
    sse = (residual * (covariance @ residual)).sum(dim=(-2, -1))
    _, logabsdet = torch.linalg.slogdet(residual)
    likelihood = 0.5 * d * torch.log(sse) - logabsdet
    padded = torch.cat([w.flatten(1), w.new_zeros((len(w), 1))], dim=1)
    blocks = padded[:, indices]
    sparsity = torch.linalg.vector_norm(blocks, dim=-1).sum(dim=(-2, -1))
    squared_adjacency = blocks.square().sum(dim=-1)
    dag = torch.diagonal(torch.matrix_exp(squared_adjacency), dim1=-2, dim2=-1).sum(-1) - indices.shape[0]
    total = likelihood + config.lambda1 * sparsity + config.lambda_dag * dag
    return total, likelihood, sparsity, dag


def fit_many(frames, names, representation, constrained, config=FitConfig(),
             categories=None, size_vars=None):
    """Batch independent fits; each has its own Adam moments and stopping state."""
    config.validate()
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    prepared = [prepare(df, names, representation, categories) for df in frames]
    sizes = prepared[0][1]
    if any(p[1] != sizes for p in prepared):
        raise ValueError("Batch requires a shared category vocabulary")
    covariance = torch.tensor(np.stack([x.T @ x / len(x) for x, _, _ in prepared]), dtype=torch.float64)
    group_mask = allowed_mask(names, constrained, size_vars)
    expanded_mask = torch.tensor(np.repeat(np.repeat(group_mask, sizes, axis=0), sizes, axis=1), dtype=torch.float64)
    indices = block_indices(sizes)
    # Zero initialization is deterministic and equivariant to category permutations.
    w = torch.zeros_like(covariance, requires_grad=True)
    optimizer = torch.optim.Adam([w], lr=config.learning_rate)
    count = len(frames)
    active = torch.ones(count, dtype=torch.bool)
    converged = np.zeros(count, dtype=bool)
    failed = np.zeros(count, dtype=bool)
    iterations = np.full(count, config.max_iter, dtype=int)
    streak = np.zeros(count, dtype=int)
    previous = np.full(count, np.nan)
    for iteration in range(1, config.max_iter + 1):
        optimizer.zero_grad()
        terms = objective(w * expanded_mask, covariance, indices, config)
        finite = torch.isfinite(torch.stack(terms)).all(dim=0)
        newly_failed = active & ~finite
        failed[newly_failed.numpy()] = True
        iterations[newly_failed.numpy()] = iteration
        active &= finite
        if not active.any():
            break
        # Select valid fits before summation; inactive parameters are restored below.
        terms[0][active].sum().backward()
        finite_grad = torch.isfinite(w.grad).all(dim=(-2, -1))
        newly_failed = active & ~finite_grad
        failed[newly_failed.numpy()] = True
        iterations[newly_failed.numpy()] = iteration
        active &= finite_grad
        with torch.no_grad():
            old = w.detach().clone()
            w.grad[~active] = 0
        optimizer.step()
        with torch.no_grad():
            w.mul_(expanded_mask)
            w[~active] = old[~active]
        if iteration % config.check_every == 0:
            with torch.no_grad():
                current = objective(w, covariance, indices, config)[0].numpy()
            relative = np.abs(current - previous) / np.maximum(1.0, np.abs(previous))
            streak = np.where(relative < config.tolerance, streak + 1, 0)
            done = active.numpy() & (streak >= config.patience)
            converged[done] = True
            iterations[done] = iteration
            active[done] = False
            previous = current
        if not active.any():
            break
    with torch.no_grad():
        terms = objective(w, covariance, indices, config)
        weights = w.numpy()
    results = []
    offsets = np.cumsum([0] + sizes)
    for k, df in enumerate(frames):
        valid = not failed[k] and all(torch.isfinite(t[k]) for t in terms)
        strengths = [[float(np.abs(weights[k, offsets[i]:offsets[i + 1], offsets[j]:offsets[j + 1]]).sum())
                      for j in range(len(names))] for i in range(len(names))]
        results.append({
            "node_names": names, "n_rows": len(df), "representation": representation,
            "constrained": constrained, "config": asdict(config), "preprocessing": prepared[k][2],
            "status": "failed" if not valid else "converged" if converged[k] else "nonconverged",
            "iterations": int(iterations[k]), "failure_reason": None if valid else "Nonfinite objective or gradient",
            "objective": {key: float(t[k]) if torch.isfinite(t[k]) else None for key, t in
                          zip(("total", "likelihood", "sparsity", "dag"), terms)},
            "weights": weights[k].tolist() if valid else None,
            "strengths": strengths if valid else None,
        })
    return results


def extract_graph(strengths, names, threshold):
    if not np.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and nonnegative")
    raw = [(a, b) for i, a in enumerate(names) for j, b in enumerate(names)
           if i != j and strengths[i][j] > threshold]
    graph = nx.DiGraph()
    graph.add_nodes_from(names)
    graph.add_edges_from(raw)
    components = list(nx.strongly_connected_components(graph))
    component = {n: k for k, nodes in enumerate(components) for n in nodes}
    converted = [(a, b) for a, b in raw if component[a] == component[b]]
    directed = [(a, b) for a, b in raw if component[a] != component[b]]
    undirected = sorted({tuple(sorted((a, b))) for a, b in converted})
    return {"thresholded_directed_edges": raw, "directed_edges": directed,
            "undirected_edges": undirected, "converted_orientations": converted,
            "cyclic_components": sorted([sorted(c) for c in components if len(c) > 1]),
            "n_directed": len(directed), "n_undirected": len(undirected),
            "other_edges": [], "n_other": 0}
