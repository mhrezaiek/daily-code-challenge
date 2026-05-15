"""Evaluate Reverse Polish Notation.

Reverse Polish Notation places each operator after its two operands, so
the expression can be evaluated with a single left-to-right pass using a
stack: push numbers; on an operator pop the right operand, then the left
operand, apply the operation, and push the result. Division truncates
toward zero, per the problem statement.
"""
from __future__ import annotations

from typing import Callable, List


def _truncating_div(a: int, b: int) -> int:
    """Integer division that truncates toward zero (matches the problem spec)."""
    quotient = abs(a) // abs(b)
    return -quotient if (a < 0) ^ (b < 0) else quotient


_OPS: dict[str, Callable[[int, int], int]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": _truncating_div,
}


def eval_rpn(tokens: List[str]) -> int:
    """Evaluate the RPN expression in ``tokens`` and return the integer result.

    Time:  O(n) — one pass over the tokens.
    Space: O(n) — operand stack.
    """
    stack: list[int] = []
    for token in tokens:
        if token in _OPS:
            right = stack.pop()
            left = stack.pop()
            stack.append(_OPS[token](left, right))
        else:
            stack.append(int(token))
    return stack[-1]


def _tests() -> None:
    # Canonical example: ((2 + 1) * 3) == 9.
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9

    # Division truncating toward zero with a leftover.
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6

    # A larger expression equivalent to ((10*(6/((9+3)*-11)))+17)+5 == 22.
    assert eval_rpn(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ) == 22

    # Single number — must be returned directly.
    assert eval_rpn(["42"]) == 42

    # Negative operands with subtraction.
    assert eval_rpn(["-5", "-3", "-"]) == -2

    # Division that truncates toward zero with a negative result (7 / -2 == -3).
    assert eval_rpn(["7", "-2", "/"]) == -3

    # Negative numerator with positive denominator (-7 / 2 == -3).
    assert eval_rpn(["-7", "2", "/"]) == -3


if __name__ == "__main__":
    _tests()
