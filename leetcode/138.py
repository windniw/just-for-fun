"""

link: https://leetcode.com/problems/copy-list-with-random-pointer

problem: 拷贝链表，每个节点多一个random指针

solution: 用字典存复制过的节点，先扫一遍复制正常链表，再扫一遍复制random指针

solution-fix: 空间压缩到O(1)，不使用字典。
              记原链表为 A -> B -> C ;
              复制自己到下一位，修改为 A -> A' -> B -> B' -> C -> C' ;
              扫一遍补上 random ;
              分离原链表

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        s = {}
        fh = Node(0, None, None)
        pa, pb = head, fh
        while pa:
            s[pa] = Node(pa.val, None, None)
            pb.next = s[pa]
            pa = pa.next
            pb = pb.next
        pa, pb = head, fh.next
        while pa:
            if pa.random:
                pb.random = s[pa.random]
            pa = pa.next
            pb = pb.next
        return fh.next
# ---
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        t = head
        while t:
            t.next = Node(t.val, t.next, None)
            t = t.next.next
        t = head
        while t:
            if t.random:
                t.next.random = t.random.next
            t = t.next.next
        fh = Node(0, None, None)
        t, ft = head, fh
        while t:
            ft.next = t.next
            ft = ft.next
            t.next = t.next.next
            t = t.next
        return fh.next