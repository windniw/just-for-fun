"""

link: https://leetcode-cn.com/problems/plus-one-linked-list

problem: 用链表记录大数，对其加一

solution: 递归栈模拟。

solution-fix: 快慢指针。寻找右边第一个不等于 9 的节点，对其加一，且对其之后连续的 9 置 0，省去栈存储空间。

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

# ---
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        t = ListNode(0)
        t.next = head

        add = t
        while head:
            if head.val != 9:
                add = head
            head = head.next

        add.val += 1
        head = add.next
        while head and head.val == 9:
            head.val = 0
            head = head.next
        return t if t.val != 0 else t.next
