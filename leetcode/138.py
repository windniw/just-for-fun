"""

link: https://leetcode.com/problems/copy-list-with-random-pointer

problem: 拷贝链表，每个节点多一个random指针

solution: 用字典存复制过的节点，先扫一遍复制正常链表，再扫一遍复制random指针

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
