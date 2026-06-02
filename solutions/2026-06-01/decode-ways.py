"""Decode Ways.

Count the number of ways to decode a digit string into letters where
A=1..Z=26. Uses bottom-up dynamic programming with O(1) rolling state:
for each position the number of decodings is the sum of decodings that
take the previous one digit (if 1..9) and the previous two digits
(if they form 10..26).
"""

from typing import List


def num_decodings(s: str) -> int:
    # Time O(n), space O(1).
    if not s or s[0] == "0":
        return 0
    n = len(s)
    prev2 = 1
    prev1 = 1
    for i in range(1, n):
        cur = 0
        one = int(s[i])
        two = int(s[i - 1 : i + 1])
        if one != 0:
            cur += prev1
        if 10 <= two <= 26:
            cur += prev2
        if cur == 0:
            return 0
        prev2, prev1 = prev1, cur
    return prev1


def _tests() -> None:
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("0") == 0
    assert num_decodings("06") == 0
    assert num_decodings("1") == 1
    assert num_decodings("11106") == 2
    assert num_decodings("27") == 1
    assert num_decodings("100") == 0


if __name__ == "__main__":
    _tests()
    print("decode-ways: all tests passed")
