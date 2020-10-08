"""

link: https://leetcode-cn.com/problems/plus-one-linked-list

problem: 用链表记录大数，对其加一

solution: 递归栈模拟。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def f(k: ListNode) -> int:
            if not k:
                return 1
            if f(k.next) == 0:
                return 0
            if k.val != 9:
                k.val += 1
                return 0
            else:
                k.val = 0
                return 1
        f(head)
        if head.val == 0:
            t = ListNode(1)
            t.next = head
            head = t
        return head

