"""Valid Parentheses.

Determine whether a string of brackets '()', '{}', '[]' is properly
matched and nested. We push each opener onto a stack and, on each closer,
verify the stack's top is the matching opener; the string is valid iff
every closer matches and the stack ends empty.
"""

from typing import Dict, List


def is_valid(s: str) -> bool:
    pairs: Dict[str, str] = {")": "(", "]": "[", "}": "{"}
    stack: List[str] = []
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


# Time: O(n) over the string length. Space: O(n) for the stack worst case.


def _tests() -> None:
    assert is_valid("") is True
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("(") is False
    assert is_valid(")") is False
    assert is_valid("((((((((((") is False


if __name__ == "__main__":
    _tests()
