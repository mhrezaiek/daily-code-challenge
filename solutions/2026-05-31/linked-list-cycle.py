"""Linked List Cycle.

Detect whether a singly linked list contains a cycle. We use Floyd's
tortoise-and-hare two-pointer algorithm: the slow pointer advances one
step and the fast pointer two; if the list is cyclic they eventually
meet, otherwise the fast pointer reaches the end.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Time: O(n) where n is the number of nodes. Space: O(1).


def _build(values: List[int], cycle_index: int = -1) -> Optional[ListNode]:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= cycle_index < len(nodes):
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


def _tests() -> None:
    assert has_cycle(None) is False
    assert has_cycle(_build([1])) is False
    assert has_cycle(_build([1, 2, 3, 4])) is False

    single_cycle = ListNode(1)
    single_cycle.next = single_cycle
    assert has_cycle(single_cycle) is True

    assert has_cycle(_build([1, 2], cycle_index=0)) is True
    assert has_cycle(_build([3, 2, 0, -4], cycle_index=1)) is True
    assert has_cycle(_build([1, 2, 3, 4, 5], cycle_index=2)) is True


if __name__ == "__main__":
    _tests()
