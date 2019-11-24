"""

link: https://leetcode.com/problems/linked-list-cycle

problem: 判断链表中是否存在环

solution: 遍历，置空

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