"""

link: https://leetcode.com/problems/reorder-list

problem: 链表重排序成 N(0) --> N(n-1) --> N(1) --> N(n-2) ... 

solution: 塞进数组重组织。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        s = []
        t = head
        while t:
            s.append(t)
            t = t.next
        for i in range(len(s) // 2):
            s[-i-1].next = s[i].next
            s[i].next = s[-i-1]
        s[len(s)//2].next = None
        return