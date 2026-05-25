# Daily Code Challenge — 2026-05-14

Solved 8 problem(s) today (two independent runs merged).

## Daily-pick run

- **Daily Temperatures** (medium, monotonic-stack) — `daily-temperatures.py`
- **Spiral Matrix** (medium, array-matrix) — `spiral-matrix.py`
- **Evaluate Reverse Polish Notation** (medium, stack) — `evaluate-rpn.py`
- **Two Sum** (easy, array-hashmap) — `two-sum.py`

## Bucketed run

| # | Bucket          | Title                                                  | Difficulty | File |
|---|-----------------|--------------------------------------------------------|------------|------|
| 1 | classic-dsa     | Longest Substring Without Repeating Characters (LC 3)  | medium     | [`classic-dsa-longest-substring-without-repeating-characters.py`](classic-dsa-longest-substring-without-repeating-characters.py) |
| 2 | trees-graphs    | Number of Provinces (LC 547)                           | medium     | [`trees-graphs-number-of-provinces.py`](trees-graphs-number-of-provinces.py) |
| 3 | ml-coding       | K-Means from scratch (NumPy only)                      | medium     | [`ml-coding-kmeans-from-scratch.py`](ml-coding-kmeans-from-scratch.py) |
| 4 | sql             | Department Top Three Salaries (LC 185)                 | hard       | [`sql-department-top-three-salaries.sql`](sql-department-top-three-salaries.sql) |

## Prompts (daily-pick run)

### Daily Temperatures

> Given an array of integers temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature.

### Spiral Matrix

> Given an m x n matrix, return all elements of the matrix in spiral order.

### Evaluate Reverse Polish Notation

> Evaluate the value of an arithmetic expression in Reverse Polish Notation.

### Two Sum

> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume each input has exactly one solution, and you may not use the same element twice.

## Notes (bucketed run)

### 1. Longest Substring Without Repeating Characters

**Summary.** Given a string, return the length of the longest substring
containing no duplicate characters.

**Approach.** Sliding window with a `last_seen[char] -> index` map. When
`s[right]` was last seen inside the current window, jump `left` to
`last_seen[ch] + 1`. The window is always duplicate-free, the running
max gives the answer.

**Complexity.** O(n) time, O(min(n, σ)) space.

### 2. Number of Provinces

**Summary.** Given an `n × n` adjacency matrix of cities, count the
number of connected components ("provinces").

**Approach.** Union-Find with path compression and union by rank.
Walk the upper triangle; `union(i, j)` for every 1. The answer is
the DSU's component count.

**Complexity.** O(n² · α(n)) time, O(n) space.

### 3. K-Means from scratch

**Summary.** Implement Lloyd's algorithm with k-means++ seeding and
empty-cluster recovery, in NumPy.

**Approach.** Vectorized pairwise distances, argmin assignment, masked
mean for the update, and empty-cluster recovery by re-seeding from the
farthest currently-assigned point. Stop when labels stabilize.

### 4. Department Top Three Salaries

**Summary.** For every department, list every employee whose salary
is one of the three highest *distinct* salaries in that department.

**Approach.** `DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY
salary DESC)`, filter `rk <= 3`, join back to `Department` for the
display name.
