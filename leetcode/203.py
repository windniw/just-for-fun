"""

link: https://leetcode.com/problems/remove-linked-list-elements

problem: 移除链表的指定元素

solution: 遍历

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fh = ListNode(0)
        fh.next = head
        prev, x = fh, fh.next
        while x:
            if x.val == val:
                prev.next = x.next
            else:
                prev = x
            x = x.next
        return fh.next