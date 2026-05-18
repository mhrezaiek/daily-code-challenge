"""
Reverse Linked List.

Approach: iterate once, repointing each node's ``next`` pointer to its
predecessor. A constant number of pointer rewires per node yields O(n) time
and O(1) extra space. An equivalent recursive form is included for reference
but the iterative version is preferred for stack-safety on long lists.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = field(default=None)


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list in place and return the new head.

    Time: O(n). Space: O(1).
    """
    prev: Optional[ListNode] = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Recursive reversal — O(n) time, O(n) stack space.

    Kept as an alternative implementation for readers; the iterative version
    is what production code should use.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def _from_iterable(values: Iterable[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def _to_list(head: Optional[ListNode]) -> list[int]:
    out: list[int] = []
    node = head
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def _tests() -> None:
    # 1. Standard case.
    assert _to_list(reverse_list(_from_iterable([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    # 2. Two-element list.
    assert _to_list(reverse_list(_from_iterable([1, 2]))) == [2, 1]

    # 3. Single-element list — no-op.
    assert _to_list(reverse_list(_from_iterable([7]))) == [7]

    # 4. Empty list.
    assert reverse_list(None) is None

    # 5. List with duplicates and negatives.
    assert _to_list(reverse_list(_from_iterable([0, -1, -1, 2, 2]))) == [2, 2, -1, -1, 0]

    # 6. Recursive variant agrees with iterative variant on a longer list.
    values = list(range(20))
    assert (
        _to_list(reverse_list_recursive(_from_iterable(values)))
        == list(reversed(values))
    )

    # 7. Reversing twice restores the original order.
    once = reverse_list(_from_iterable([3, 1, 4, 1, 5, 9, 2, 6]))
    twice = reverse_list(once)
    assert _to_list(twice) == [3, 1, 4, 1, 5, 9, 2, 6]

    print("reverse-linked-list: all tests passed")


if __name__ == "__main__":
    _tests()
