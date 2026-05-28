"""Happy Number.

A number is happy if repeatedly replacing it by the sum of the squares of its
digits eventually reaches 1; otherwise the process enters a cycle. We detect
the cycle with Floyd's tortoise-and-hare algorithm, which uses O(1) extra
memory and avoids the hash-set bookkeeping.
"""


def _sum_of_squares(n: int) -> int:
    total = 0
    while n > 0:
        n, d = divmod(n, 10)
        total += d * d
    return total


def is_happy(n: int) -> bool:
    # Time: O(log n) per step, terminates in a bounded number of steps because
    # values quickly fall below ~243 (the max square-sum for 3-digit numbers).
    # Space: O(1).
    if n <= 0:
        return False
    slow = n
    fast = _sum_of_squares(n)
    while fast != 1 and slow != fast:
        slow = _sum_of_squares(slow)
        fast = _sum_of_squares(_sum_of_squares(fast))
    return fast == 1


def _tests() -> None:
    assert is_happy(1) is True
    assert is_happy(19) is True
    assert is_happy(7) is True
    assert is_happy(2) is False
    assert is_happy(4) is False
    assert is_happy(100) is True
    assert is_happy(0) is False
    assert is_happy(10) is True


if __name__ == "__main__":
    _tests()
