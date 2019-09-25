"""

link: https://leetcode.com/problems/rotate-list

problem: 右移链表k位

solution: 遍历一次求长度，取模拿断开点break_point，令tail.next = head, break_point.next = None

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        tail = head
        length = 1
        while tail.next is not None:
            length += 1
            tail = tail.next
        tail.next = head
        for i in range(length - k % length - 1):
            head = head.next
        res = head.next
        head.next = None
        return res