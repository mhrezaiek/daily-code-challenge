"""LRU Cache.

O(1) get/put implementation using a hash map keyed by ``key`` whose values
are nodes in a doubly linked list. The list is ordered most-recently-used
at the head and least-recently-used at the tail; touching a node moves
it to the head, and on overflow the tail is evicted.
"""

from typing import Dict, Optional


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUCache:
    # All operations: O(1) time, O(capacity) space.

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._map: Dict[int, _Node] = {}
        # Sentinel head/tail simplifies edge cases.
        self._head = _Node(0, 0)
        self._tail = _Node(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node) -> None:
        assert node.prev is not None and node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: _Node) -> None:
        node.prev = self._head
        node.next = self._head.next
        assert self._head.next is not None
        self._head.next.prev = node
        self._head.next = node

    def get(self, key: int) -> int:
        node = self._map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        existing = self._map.get(key)
        if existing is not None:
            existing.value = value
            self._remove(existing)
            self._add_to_front(existing)
            return
        if len(self._map) >= self.capacity:
            lru = self._tail.prev
            assert lru is not None and lru is not self._head
            self._remove(lru)
            del self._map[lru.key]
        node = _Node(key, value)
        self._add_to_front(node)
        self._map[key] = node


def _tests() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Update existing key does not evict.
    c2 = LRUCache(2)
    c2.put(1, 10)
    c2.put(2, 20)
    c2.put(1, 11)
    c2.put(3, 30)  # evicts 2, since 1 was just used
    assert c2.get(2) == -1
    assert c2.get(1) == 11
    assert c2.get(3) == 30

    # Capacity-1 edge case.
    c3 = LRUCache(1)
    c3.put(1, 1)
    c3.put(2, 2)
    assert c3.get(1) == -1
    assert c3.get(2) == 2

    # Missing key returns -1.
    c4 = LRUCache(3)
    assert c4.get(42) == -1

    # Invalid capacity rejected.
    try:
        LRUCache(0)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for capacity=0")

    # Negative values work fine.
    c5 = LRUCache(2)
    c5.put(1, -1)
    c5.put(2, -2)
    assert c5.get(1) == -1
    assert c5.get(2) == -2


if __name__ == "__main__":
    _tests()
