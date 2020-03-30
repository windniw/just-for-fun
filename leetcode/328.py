"""

link: https://leetcode.com/problems/odd-even-linked-list

problem: 给链表，要求拆分成奇数项在前，偶数项在后的形式，时间O(n)，空间O(1)

solution: 拆链表保存奇偶项表头和表尾

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head, odd_tail, even_head, even_tail, cnt = head, head, head.next, head.next, 3

        t = head.next.next
        while t:
            k = t
            t = t.next
            if cnt & 1:
                odd_tail.next = k
                odd_tail = k
            else:
                even_tail.next = k
                even_tail = k
            cnt += 1
        odd_tail.next = even_head
        even_tail.next = None
        return odd_head
