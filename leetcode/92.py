"""

link: https://leetcode.com/problems/reverse-linked-list-ii

problem: 原地旋转链表的 [m,n]

solution: 常规操作

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None: return head
        fh = ListNode(0)
        fh.next = head
        t = fh
        for i in range(m - 1):
            t = t.next
        rh, rt, k = t.next, t.next, t.next.next
        for i in range(m, n):
            tmp = k
            k = k.next
            tmp.next = rh
            rh = tmp
        t.next = rh
        rt.next = k
        return fh.next