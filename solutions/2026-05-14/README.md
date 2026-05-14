# Daily Code Challenge — 2026-05-14

Solved **4 problems** across 4 buckets (classic DSA, trees & graphs,
ML-coding, SQL). Difficulty mix: 3 medium + 1 hard.

| # | Bucket          | Title                                                  | Difficulty | File |
|---|-----------------|--------------------------------------------------------|------------|------|
| 1 | classic-dsa     | Longest Substring Without Repeating Characters (LC 3)  | medium     | [`classic-dsa-longest-substring-without-repeating-characters.py`](classic-dsa-longest-substring-without-repeating-characters.py) |
| 2 | trees-graphs    | Number of Provinces (LC 547)                           | medium     | [`trees-graphs-number-of-provinces.py`](trees-graphs-number-of-provinces.py) |
| 3 | ml-coding       | K-Means from scratch (NumPy only)                      | medium     | [`ml-coding-kmeans-from-scratch.py`](ml-coding-kmeans-from-scratch.py) |
| 4 | sql             | Department Top Three Salaries (LC 185)                 | hard       | [`sql-department-top-three-salaries.sql`](sql-department-top-three-salaries.sql) |

---

## 1. Longest Substring Without Repeating Characters

**Summary.** Given a string, return the length of the longest substring
containing no duplicate characters.

**Approach.** Sliding window with a `last_seen[char] -> index` map. When
`s[right]` was last seen inside the current window, jump `left` to
`last_seen[ch] + 1`. The window is always duplicate-free, the running
max gives the answer.

**Why this approach over alternatives.** Two-pointer + set works but
shrinks the window one step at a time; the "jump to last_seen + 1"
trick collapses that into O(1) per character.

**Complexity.** O(n) time, O(min(n, σ)) space.

**Pitfall.** The `last_seen[ch] >= left` guard matters — without it,
`"abba"` would incorrectly rewind `left` to a stale position.

---

## 2. Number of Provinces

**Summary.** Given an `n × n` adjacency matrix of cities, count the
number of connected components ("provinces").

**Approach.** Union-Find with path compression and union by rank.
Walk the upper triangle; `union(i, j)` for every 1. The answer is
the DSU's component count.

**Why this approach over alternatives.** BFS/DFS solve it in the same
O(n²) but Union-Find is the canonical pattern for incremental
connectivity questions (Accounts Merge, Most Stones Removed,
Satisfiability of Equality Equations all reuse the same scaffold).

**Complexity.** O(n² · α(n)) time, O(n) space.

**Pitfall.** Recursive `find` blows the stack at n ≈ 1e6. The
iterative two-pass implementation here keeps recursion depth at 0.

---

## 3. K-Means from scratch

**Summary.** Implement Lloyd's algorithm with k-means++ seeding and
empty-cluster recovery, in NumPy.

**Approach.** Vectorized pairwise distances using
`||x − c||² = ||x||² + ||c||² − 2 x·c`. Assignment via `argmin`,
update via masked mean. Empty clusters re-seed from the farthest
currently-assigned point. Stop when labels stabilize.

**Why this approach over alternatives.** A naive Python loop over
points is O(n · k · d) per iteration with huge constants; the einsum
form is the same big-O but ~50× faster in practice. k-means++ keeps
convergence stable across seeds — interviewers expect this over
uniform random init.

**Numerical / convergence notes.**
- Clip the expanded distance at 0 — floating-point error can drive it
  slightly negative.
- Detect convergence on label equality (one iteration earlier than a
  centroid-epsilon check, and more robust under cluster re-seeding).
- Cross-check against `sklearn.cluster.KMeans` inertia when available;
  on clean blobs ours lands within 10% of theirs.

**Pitfall.** Forgetting empty-cluster handling — a single empty
cluster causes a NaN centroid and cascading failure on the next
iteration.

---

## 4. Department Top Three Salaries

**Summary.** For every department, list every employee whose salary
is one of the three highest *distinct* salaries in that department.
Ties at any rank are kept.

**Approach.** `DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY
salary DESC)`, filter `rk <= 3`, join back to `Department` for the
display name.

**Why DENSE_RANK and not RANK / ROW_NUMBER.**
- `ROW_NUMBER` drops tied salaries arbitrarily — wrong answer.
- `RANK` skips ranks after ties, so two #1s mean no #2 — also wrong.
- `DENSE_RANK` keeps "top 3 *distinct* salaries", which is what the
  problem specifies.

**Complexity.** O(n log n) for the window sort within each partition,
plus an O(n) hash join to the small `Department` table.

**Pitfall.** Reaching for `LIMIT 3` per group is tempting but
mishandles ties — DENSE_RANK is the safe pattern.
