"""

link: https://leetcode.com/problems/reverse-linked-list

problem: 翻转链表，要求用循环和递归两种方式

solution: 水

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        while head:
            x = head.next
            head.next = res
            res = head
            head = x
        return res
# ---
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        x = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return x