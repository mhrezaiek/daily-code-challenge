"""
Number of Provinces (LeetCode 547)
----------------------------------
Source: https://leetcode.com/problems/number-of-provinces/

There are n cities. Some pairs are connected directly; if A is connected
to B and B to C then A is indirectly connected to C. A province is a
group of directly or indirectly connected cities.

Given an n x n adjacency matrix `isConnected` (1 = edge, 0 = none),
return the total number of provinces.

Approach: Union-Find (disjoint set union) with path compression and
union by rank. Walk the upper triangle of the matrix; for every edge,
`union` the two endpoints. The answer is the number of distinct roots.

Why this approach: DFS / BFS also work in O(n^2) but Union-Find is the
canonical answer for incremental connectivity questions (and it
generalizes when edges arrive online). It's also good practice for
problems like Accounts Merge and Most Stones Removed.

Complexity: O(n^2 * alpha(n)) time, O(n) space. alpha is the inverse
Ackermann function — effectively constant for any practical n.
"""
from __future__ import annotations
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        # Iterative path compression — flattens the tree, no recursion depth risk.
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # Union by rank: attach shorter tree under taller one.
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True


def find_circle_num(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                dsu.union(i, j)
    return dsu.components


def _tests() -> None:
    # Example 1: 2 provinces — {0,1}, {2}
    m1 = [[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1]]
    assert find_circle_num(m1) == 2

    # Example 2: 3 provinces — all isolated
    m2 = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]
    assert find_circle_num(m2) == 3

    # Single city
    assert find_circle_num([[1]]) == 1

    # Fully connected — one province
    m4 = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
    assert find_circle_num(m4) == 1

    # Two chains: 0-1-2 and 3-4 -> 2 provinces
    m5 = [[1, 1, 0, 0, 0],
          [1, 1, 1, 0, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 1, 1]]
    assert find_circle_num(m5) == 2

    # Stress: identity matrix, n = 50 — every city is its own province
    n = 50
    big = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    assert find_circle_num(big) == n

    print("find_circle_num: all tests passed")


if __name__ == "__main__":
    _tests()

# Time:  O(n^2 * alpha(n)) — alpha(n) is effectively constant.
# Space: O(n) for the DSU.
