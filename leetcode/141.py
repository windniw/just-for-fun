"""

link: https://leetcode.com/problems/linked-list-cycle

problem: 判断链表中是否存在环

solution: 遍历，置空

solution-fix: 快慢指针

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == float("inf"):
                return True
            head.val = float("inf")
            head = head.next
        return False
#---
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        fast, slow = head.next, head
        while fast and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return fast == slow