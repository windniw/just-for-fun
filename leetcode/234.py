"""

link: https://leetcode.com/problems/palindrome-linked-list

problem: 判断链表是否回文，要求时间O(n)，空间O(1)

solution: 快慢指针找中点，沿中点向后翻转后半截，然后比较两段

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            t = slow.next
            slow.next = prev
            prev = slow
            slow = t

        while prev and head:
            if prev.val == head.val:
                prev, head = prev.next, head.next
            else:
                return False
        return True