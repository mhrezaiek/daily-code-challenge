"""Course Schedule.

Determine whether all courses can be finished given prerequisite pairs.
Approach: build a directed graph and detect cycles using Kahn's algorithm
(BFS over nodes with zero in-degree). All courses are finishable iff the
topological order covers every node.
"""

from collections import defaultdict, deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # Time: O(V + E)  Space: O(V + E)
    graph: dict[int, list[int]] = defaultdict(list)
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue: deque[int] = deque(i for i in range(num_courses) if in_degree[i] == 0)
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses


def _tests() -> None:
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False
    assert can_finish(5, []) is True
    assert can_finish(6, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]]) is True


if __name__ == "__main__":
    _tests()
