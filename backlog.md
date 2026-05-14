# Backlog

Running list of researched problems queued for future days. Removed when solved (and recorded in `solved-index.md`).

---

## [easy] Two Sum
- Bucket: classic-dsa
- Source: https://leetcode.com/problems/two-sum/
- Tags: array, hashmap
- Added: 2026-05-14
- Statement: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Each input has exactly one solution, and you may not use the same element twice.

## [medium] Number of Connected Components in an Undirected Graph (LC 323)
- Bucket: trees-graphs
- Source: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
- Tags: union-find, dfs
- Added: 2026-05-14
- Statement: Given `n` nodes labeled 0..n-1 and a list of undirected edges, return the number of connected components in the graph.

## [hard] Sliding Window Maximum (LC 239)
- Bucket: classic-dsa
- Source: https://leetcode.com/problems/sliding-window-maximum/
- Tags: deque, monotonic-queue, sliding-window
- Added: 2026-05-14
- Statement: Given an integer array `nums` and a window size `k`, return the maximum element of every window of size `k` as the window slides from left to right.

## [medium] Implement Logistic Regression from scratch
- Bucket: ml-coding
- Source: https://www.tryexponent.com/blog/top-python-machine-learning-interview-questions
- Tags: numpy, gradient-descent, classification
- Added: 2026-05-14
- Statement: Using NumPy only, implement binary logistic regression with gradient descent. Functions: `fit(X, y, lr, epochs)` returning weights and bias; `predict_proba(X)`; `predict(X)`. Include L2 regularization as an optional parameter, and verify on a small linearly-separable synthetic dataset.

## [medium] Nth Highest Salary (LC 177)
- Bucket: sql
- Source: https://leetcode.com/problems/nth-highest-salary/
- Tags: window-functions, dense_rank
- Added: 2026-05-14
- Statement: Write a SQL function `getNthHighestSalary(N INT)` that returns the `N`-th highest distinct salary from the `Employee` table. If there are fewer than `N` distinct salaries, return `NULL`.

## [medium] Rotting Oranges (LC 994)
- Bucket: trees-graphs
- Source: https://leetcode.com/problems/rotting-oranges/
- Tags: bfs, grid
- Added: 2026-05-14
- Statement: In a grid where 0 = empty, 1 = fresh orange, 2 = rotten, every minute any fresh orange adjacent (4-dir) to a rotten one becomes rotten. Return the minimum number of minutes until no fresh orange remains, or -1 if impossible.

## [medium] Implement k-NN classifier from scratch
- Bucket: ml-coding
- Source: https://www.tryexponent.com/blog/top-python-machine-learning-interview-questions
- Tags: numpy, classification, distance
- Added: 2026-05-14
- Statement: Implement a `KNN(k)` classifier with `fit(X, y)` and `predict(X)` using vectorized Euclidean distance. Verify on the Iris dataset against `sklearn.neighbors.KNeighborsClassifier`.

## [medium] Pandas — Department Top Three Salaries
- Bucket: pandas
- Source: https://leetcode.com/problems/department-top-three-salaries/ (Pandas variant)
- Tags: groupby, rank, dense_rank
- Added: 2026-05-14
- Statement: Solve LC 185 using only Pandas (no SQL). Function signature `top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame`.

## [medium] LRU Cache (LC 146)
- Bucket: system-design-adjacent
- Source: https://leetcode.com/problems/lru-cache/
- Tags: hashmap, doubly-linked-list, design
- Added: 2026-05-14
- Statement: Design an LRU cache with `get(key)` and `put(key, value)` both in O(1). Already exists in `questions.json/active_pool`; included here for the system-design rotation.
