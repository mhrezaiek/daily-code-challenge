"""Merge Two Sorted Lists.

Merge two ascending-sorted singly linked lists into one sorted list.
Approach: walk both lists with two pointers using a dummy head; splice the
smaller current node onto the result, then attach the remaining tail of
whichever list still has nodes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    # Time: O(n + m)  Space: O(1) extra
    dummy = ListNode(0)
    tail = dummy
    a, b = l1, l2
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next


def _from_list(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def _to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def _tests() -> None:
    assert _to_list(merge_two_lists(_from_list([1, 2, 4]), _from_list([1, 3, 4]))) == [
        1,
        1,
        2,
        3,
        4,
        4,
    ]
    assert _to_list(merge_two_lists(None, None)) == []
    assert _to_list(merge_two_lists(None, _from_list([0]))) == [0]
    assert _to_list(merge_two_lists(_from_list([5]), None)) == [5]
    assert _to_list(merge_two_lists(_from_list([-3, -1, 2]), _from_list([-2, 0, 4]))) == [
        -3,
        -2,
        -1,
        0,
        2,
        4,
    ]
    assert _to_list(merge_two_lists(_from_list([1, 1, 1]), _from_list([1, 1]))) == [
        1,
        1,
        1,
        1,
        1,
    ]
    assert _to_list(merge_two_lists(_from_list([1, 5, 9]), _from_list([2, 3, 4]))) == [
        1,
        2,
        3,
        4,
        5,
        9,
    ]


if __name__ == "__main__":
    _tests()
