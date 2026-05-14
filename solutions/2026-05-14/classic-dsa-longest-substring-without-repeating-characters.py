"""
Longest Substring Without Repeating Characters (LeetCode 3)
-----------------------------------------------------------
Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, return the length of the longest substring without
repeating characters.

Approach: classic sliding window with a "last seen index" hashmap.
    - Maintain a window [left, right]. Walk `right` over the string.
    - On each step, if s[right] has been seen at index >= left, jump
      `left` to last_seen[s[right]] + 1 so the window stays unique.
    - Track the running max width.

Why this approach: O(n) time with O(min(n, sigma)) space, single pass.
Two-pointer + set works but does extra hops to shrink the window;
the "jump to last_seen + 1" trick avoids that and is cleaner.

Complexity: O(n) time, O(min(n, alphabet_size)) space.
"""
from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        # If we've seen `ch` inside the current window, jump `left` past it.
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best


def _tests() -> None:
    cases = [
        ("abcabcbb", 3),     # "abc"
        ("bbbbb", 1),
        ("pwwkew", 3),       # "wke"
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),         # "vdf"
        ("anviaj", 5),       # "nviaj"
        ("tmmzuxt", 5),      # "mzuxt"
        ("abba", 2),         # ensure `left` never moves backward
    ]
    for s, expected in cases:
        got = length_of_longest_substring(s)
        assert got == expected, f"length_of_longest_substring({s!r}) = {got}, want {expected}"
    print("length_of_longest_substring: all tests passed")


if __name__ == "__main__":
    _tests()

# Time:  O(n) — each index is visited at most twice (right pointer + the
#               implicit jump via last_seen).
# Space: O(min(n, sigma)) for the last_seen dict.
