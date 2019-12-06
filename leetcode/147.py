"""

link: https://leetcode.com/problems/insertion-sort-list

problem: 对链表实现插入排序

solution: 模拟

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        fh = ListNode(0)
        fh.next = head
        pre, cur = head, head.next
        while cur:
            if cur.val >= pre.val:
                pre = cur
                cur = cur.next
                continue
            t = cur
            pre.next = cur.next
            cur = cur.next
            th = fh
            while th.next.val < t.val:
                th = th.next
            t.next = th.next
            th.next = t
        return fh.next