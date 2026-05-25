"""
K-Means Clustering — implement from scratch (NumPy only)
--------------------------------------------------------
Sources:
    - Lloyd's algorithm: https://en.wikipedia.org/wiki/K-means_clustering
    - K-means++ seeding: Arthur & Vassilvitskii, 2007.
    - Common ML-coding interview problem:
      https://www.tryexponent.com/blog/top-python-machine-learning-interview-questions

Task
----
Implement `kmeans(X, k, max_iter, seed)` that returns:
    - centroids: (k, d) array of final centroid positions
    - labels:    (n,) array of cluster indices in [0, k)
    - n_iter:    number of iterations actually run

Constraints
-----------
- NumPy only (no sklearn for the implementation).
- Use k-means++ seeding for stable initialization.
- Stop early when labels stop changing (or after max_iter).
- Handle empty clusters by re-seeding from the farthest assigned point.

Algorithm (Lloyd's, vectorized)
-------------------------------
1. Seed k centroids with k-means++.
2. Repeat:
   a. Assign every point to the nearest centroid (vectorized
      pairwise distances via the (a-b)^2 = a^2 + b^2 - 2 a.b identity).
   b. Recompute each centroid as the mean of its assigned points.
      If a cluster is empty, re-seed it from the farthest point in
      its current cluster's assigned points.
   c. Stop when assignments don't change or `max_iter` is reached.

Complexity: O(n * k * d * n_iter) time, O(n * k) extra space for the
distance matrix.
"""
from __future__ import annotations
import numpy as np
from typing import Tuple


def _pairwise_sq_dists(X: np.ndarray, C: np.ndarray) -> np.ndarray:
    """Squared Euclidean distance matrix, shape (n, k). Fully vectorized."""
    # ||x - c||^2 = ||x||^2 + ||c||^2 - 2 x.c
    x2 = np.einsum("ij,ij->i", X, X)[:, None]   # (n, 1)
    c2 = np.einsum("ij,ij->i", C, C)[None, :]   # (1, k)
    cross = X @ C.T                              # (n, k)
    # Clip for tiny negative values from floating-point error.
    return np.maximum(x2 + c2 - 2.0 * cross, 0.0)


def _kmeans_pp_init(X: np.ndarray, k: int, rng: np.random.Generator) -> np.ndarray:
    n = X.shape[0]
    first = rng.integers(0, n)
    centers = [X[first].copy()]
    closest_sq = np.sum((X - centers[0]) ** 2, axis=1)
    for _ in range(1, k):
        total = closest_sq.sum()
        if total == 0:
            # All points coincide with chosen centers — fall back to uniform.
            idx = rng.integers(0, n)
        else:
            probs = closest_sq / total
            idx = rng.choice(n, p=probs)
        centers.append(X[idx].copy())
        new_sq = np.sum((X - centers[-1]) ** 2, axis=1)
        closest_sq = np.minimum(closest_sq, new_sq)
    return np.asarray(centers, dtype=X.dtype)


def kmeans(
    X: np.ndarray,
    k: int,
    max_iter: int = 100,
    seed: int | None = None,
) -> Tuple[np.ndarray, np.ndarray, int]:
    if k <= 0:
        raise ValueError("k must be positive")
    if X.ndim != 2:
        raise ValueError("X must be 2D (n_samples, n_features)")
    n = X.shape[0]
    if k > n:
        raise ValueError("k cannot exceed number of samples")

    rng = np.random.default_rng(seed)
    X = X.astype(np.float64, copy=False)
    centroids = _kmeans_pp_init(X, k, rng)
    labels = np.full(n, -1, dtype=np.int64)

    for it in range(1, max_iter + 1):
        # Assignment step.
        d2 = _pairwise_sq_dists(X, centroids)
        new_labels = np.argmin(d2, axis=1)

        if np.array_equal(new_labels, labels):
            return centroids, new_labels, it
        labels = new_labels

        # Update step.
        new_centroids = np.empty_like(centroids)
        for j in range(k):
            mask = labels == j
            if mask.any():
                new_centroids[j] = X[mask].mean(axis=0)
            else:
                # Empty cluster -> re-seed from the point currently
                # farthest from its assigned centroid (standard recovery).
                far_idx = int(np.argmax(d2[np.arange(n), labels]))
                new_centroids[j] = X[far_idx]
        centroids = new_centroids

    return centroids, labels, max_iter


def inertia(X: np.ndarray, centroids: np.ndarray, labels: np.ndarray) -> float:
    """Sum of squared distances of samples to their cluster centers."""
    diff = X - centroids[labels]
    return float(np.sum(diff * diff))


def _make_blobs(n_per: int, centers: np.ndarray, std: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    chunks = [c + rng.normal(scale=std, size=(n_per, c.size)) for c in centers]
    return np.vstack(chunks)


def _tests() -> None:
    # Three well-separated blobs in 2D.
    true_centers = np.array([[0.0, 0.0], [10.0, 0.0], [0.0, 10.0]])
    X = _make_blobs(n_per=80, centers=true_centers, std=0.4, seed=42)

    centroids, labels, n_iter = kmeans(X, k=3, max_iter=100, seed=0)
    assert centroids.shape == (3, 2)
    assert labels.shape == (240,)
    assert set(labels.tolist()) == {0, 1, 2}

    # Every recovered centroid should match one true center to within 0.3.
    matched = set()
    for c in centroids:
        dists = np.linalg.norm(true_centers - c, axis=1)
        j = int(np.argmin(dists))
        assert dists[j] < 0.3, f"centroid {c} not near any true center"
        matched.add(j)
    assert matched == {0, 1, 2}, "did not recover all three blobs"

    # k = 1 collapses to the global mean.
    c1, l1, _ = kmeans(X, k=1, seed=0)
    assert l1.tolist() == [0] * X.shape[0]
    assert np.allclose(c1[0], X.mean(axis=0))

    # Identical points -> all collapse onto that point.
    X_dup = np.zeros((20, 3))
    c_dup, _l, _ = kmeans(X_dup, k=2, seed=1)
    assert np.allclose(c_dup, 0.0)

    # Optional: compare inertia with sklearn if available.
    try:
        from sklearn.cluster import KMeans
        sk = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
        ours = inertia(X, centroids, labels)
        theirs = float(sk.inertia_)
        # On clean blobs both should reach near-identical local optima.
        assert abs(ours - theirs) / max(theirs, 1.0) < 0.10, (
            f"our inertia {ours:.2f} too far from sklearn's {theirs:.2f}"
        )
    except ImportError:
        pass  # sklearn not available — skip the cross-check.

    print(f"kmeans: all tests passed (converged in {n_iter} iters)")


if __name__ == "__main__":
    _tests()

# Time:  O(n * k * d) per iteration -> O(n * k * d * n_iter) total.
# Space: O(n * k) for the distance matrix + O(k * d) for centroids.
#
# Numerical / convergence notes:
#   - The (a-b)^2 expansion is clipped at 0 to guard against negative
#     values from floating-point error.
#   - Convergence is detected via label equality rather than a centroid
#     epsilon — labels stabilize one iteration earlier and equality is
#     a more reliable signal under empty-cluster re-seeding.
