"""Min Stack.

Use two parallel stacks: the main values and a running minimum stack. On each
push, append the smaller of (new value, current min) to the min stack so the
current minimum is always at the top of the min stack. All operations are O(1).
"""

from __future__ import annotations

from typing import List


class MinStack:
    # All operations are O(1) time, O(n) total space.

    def __init__(self) -> None:
        self._values: List[int] = []
        self._mins: List[int] = []

    def push(self, val: int) -> None:
        self._values.append(val)
        if self._mins:
            self._mins.append(min(val, self._mins[-1]))
        else:
            self._mins.append(val)

    def pop(self) -> None:
        if not self._values:
            raise IndexError("pop from empty stack")
        self._values.pop()
        self._mins.pop()

    def top(self) -> int:
        if not self._values:
            raise IndexError("top from empty stack")
        return self._values[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("get_min from empty stack")
        return self._mins[-1]


def _tests() -> None:
    # Basic push / top / get_min.
    s = MinStack()
    s.push(5)
    assert s.top() == 5
    assert s.get_min() == 5

    # Min should track decreases.
    s.push(3)
    assert s.get_min() == 3
    s.push(7)
    assert s.get_min() == 3
    s.push(1)
    assert s.get_min() == 1

    # Pop should restore prior min.
    s.pop()
    assert s.get_min() == 3
    s.pop()
    assert s.get_min() == 3
    s.pop()
    assert s.get_min() == 5
    assert s.top() == 5

    # Duplicates: same min appearing twice survives one pop.
    s2 = MinStack()
    s2.push(2)
    s2.push(2)
    s2.push(2)
    assert s2.get_min() == 2
    s2.pop()
    assert s2.get_min() == 2
    s2.pop()
    assert s2.get_min() == 2
    s2.pop()

    # Negatives.
    s3 = MinStack()
    s3.push(-1)
    s3.push(-5)
    s3.push(0)
    assert s3.get_min() == -5
    s3.pop()
    assert s3.get_min() == -5
    s3.pop()
    assert s3.get_min() == -1

    # Empty stack errors.
    empty = MinStack()
    for op in (empty.pop, empty.top, empty.get_min):
        try:
            op()
        except IndexError:
            continue
        raise AssertionError(f"expected IndexError from {op.__name__}")

    # Single-element lifecycle.
    s4 = MinStack()
    s4.push(42)
    assert s4.top() == 42
    assert s4.get_min() == 42
    s4.pop()
    try:
        s4.top()
    except IndexError:
        pass
    else:
        raise AssertionError("expected empty stack after pop")


if __name__ == "__main__":
    _tests()
