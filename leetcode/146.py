"""

link: https://leetcode.com/problems/lru-cache

problem: 实现一个LRU缓存，要求时间O(1)

solution: 哈希 + 双向链表

"""
class LinkNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store:
            x = self.store[key]
            if x == self.tail:
                return x.val
            if x == self.head:
                self.head = x.next
            if x.prev:
                x.prev.next = x.next
            if x.next:
                x.next.prev = x.prev
            self.tail.next = x
            x.prev = self.tail
            x.next = None
            self.tail = x
            return x.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].val = value
            self.get(key)
        else:
            x = LinkNode(key, value)
            if self.tail:
                self.tail.next = x
                x.prev = self.tail
            else:
                self.head = self.tail = x
            self.tail = x
            self.store[key] = x
            if len(self.store) > self.capacity:
                self.store.pop(self.head.key)
                self.head = self.head.next
