"""

link: https://leetcode.com/problems/sort-list

problem: 链表排序，要求时间 O(nlogn), 空间O(1)

solution: 归并排序，用快慢指针找到链表中点

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        t = slow.next
        slow.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(t)
        fh = ListNode(0)
        cur = fh
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        if h2:
            cur.next = h2
        return fh.next
