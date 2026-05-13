"""Word Break.

Return True iff string s can be segmented into a sequence of dictionary
words. We use bottom-up DP: dp[i] is True when s[:i] is segmentable. For
each i we look back at every j < i where dp[j] is True and check whether
s[j:i] is in the dictionary. A set lookup keeps the inner check O(1), so
the overall complexity is O(n^2) time / O(n) space.
"""

from __future__ import annotations

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """Return True if s can be segmented into words from word_dict.

    Time:  O(n^2) where n = len(s) (with O(1) substring hashing assumed)
    Space: O(n)
    """
    if not s:
        return True
    words = set(word_dict)
    # Skip impossible substring lengths by tracking the dictionary's max word.
    max_len = max((len(w) for w in words), default=0)
    if max_len == 0:
        return False

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # the empty prefix is always segmentable
    for i in range(1, n + 1):
        # Only look back up to max_len characters; longer slices can't match.
        lo = max(0, i - max_len)
        for j in range(lo, i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


def _tests() -> None:
    # Canonical LeetCode examples.
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    # Empty string is trivially segmentable.
    assert word_break("", ["a", "b"]) is True

    # Single-character dictionary covers the string.
    assert word_break("aaaa", ["a"]) is True
    # ...but not if the only word is longer than the string.
    assert word_break("aaaa", ["aaaaa"]) is False

    # Overlapping words: must choose the right split.
    assert word_break("aaaaaaa", ["aaaa", "aaa"]) is True

    # Adversarial case where greedy would fail but DP succeeds.
    assert (
        word_break(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            ["a", "aa", "aaa", "aaaa", "aaaaa"],
        )
        is False
    )

    # Empty dictionary rejects any non-empty string.
    assert word_break("anything", []) is False


if __name__ == "__main__":
    _tests()
    print("word_break: all tests passed")
