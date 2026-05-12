"""
Coin Change (LC 322)
--------------------
Given an integer array `coins` and an integer `amount`, return the fewest
number of coins needed to make up `amount`. Return -1 if it can't be made.
You have an infinite supply of each coin type.

Approach: bottom-up DP.
    dp[a] = min coins to make amount a
    dp[0] = 0
    dp[a] = min(dp[a - c] + 1) for each coin c <= a
    Answer: dp[amount] if reachable else -1.

Complexity: O(amount * len(coins)) time, O(amount) space.

A BFS variant is included for completeness — same complexity in the worst
case but often faster in practice because it stops at the first level
that reaches `amount`.
"""
from __future__ import annotations
from collections import deque
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def coin_change_bfs(coins: List[int], amount: int) -> int:
    """Alternative BFS solution — useful when amount is small and coins are dense."""
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    seen = {0}
    q = deque([(0, 0)])  # (current_sum, steps)
    while q:
        s, steps = q.popleft()
        for c in coins:
            ns = s + c
            if ns == amount:
                return steps + 1
            if ns < amount and ns not in seen:
                seen.add(ns)
                q.append((ns, steps + 1))
    return -1


def _tests() -> None:
    cases = [
        ([1, 2, 5], 11, 3),         # 5 + 5 + 1
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 2, 2),
        ([2, 5, 10, 1], 27, 4),     # 10 + 10 + 5 + 2
        ([186, 419, 83, 408], 6249, 20),  # classic stress test
        ([1, 2, 5], 100, 20),
    ]
    for coins, amount, expected in cases:
        got = coin_change(coins, amount)
        assert got == expected, f"coin_change({coins}, {amount}) = {got}, want {expected}"
        # BFS must agree (skip the heavy 6249 case — exponential frontier).
        if amount <= 100:
            got_bfs = coin_change_bfs(coins, amount)
            assert got_bfs == expected, f"coin_change_bfs({coins}, {amount}) = {got_bfs}"
    print("coin_change: all tests passed")


if __name__ == "__main__":
    _tests()
