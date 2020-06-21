"""

link: https://leetcode.com/problems/add-two-numbers-ii

problem: 链表存数字，大数加法，不许直接翻转链表

solution: 转栈再加

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2, s3 = [], [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        n = 0
        while s1 or s2 or n:
            t = (s1.pop() if s1 else 0) + (s2.pop() if s2 else 0) + n
            s3.append(t % 10)
            n = t // 10
        head = ListNode(0)
        cur = head
        for x in reversed(s3):
            cur.next = ListNode(x)
            cur = cur.next
        return head.next
