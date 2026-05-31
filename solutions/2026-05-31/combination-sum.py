"""Combination Sum.

Given an array of distinct positive integers ``candidates`` and a target,
return every unique combination of candidates that sums to ``target``.
Each candidate may be chosen unlimited times. We solve with backtracking:
sort the candidates, recurse from a starting index to avoid permutations,
and prune branches once the running sum exceeds the target.
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)
    results: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path.copy())
            return
        for i in range(start, len(candidates)):
            value = candidates[i]
            if value > remaining:
                break
            path.append(value)
            backtrack(i, remaining - value)
            path.pop()

    backtrack(0, target)
    return results


# Time: O(N^(T/M)) where N=len(candidates), T=target, M=min(candidates).
# Space: O(T/M) for the recursion depth (excluding output).


def _tests() -> None:
    def normalize(combos):
        return sorted(tuple(sorted(c)) for c in combos)

    assert normalize(combination_sum([2, 3, 6, 7], 7)) == normalize([[2, 2, 3], [7]])
    assert normalize(combination_sum([2, 3, 5], 8)) == normalize(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    assert combination_sum([2], 1) == []
    assert combination_sum([1], 1) == [[1]]
    assert combination_sum([1], 2) == [[1, 1]]
    assert combination_sum([8, 4, 6], 3) == []
    assert normalize(combination_sum([2, 3, 5], 0)) == [()]


if __name__ == "__main__":
    _tests()
