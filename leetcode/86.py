"""

link: https://leetcode.com/problems/partition-list

problem: 修改链表，使得比x小的值都在x之前

solution: 双指针扫

"""

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None: return head
        _head = ListNode(0)
        _head.next = head
        i = _head
        while i.next and i.next.val < x:
            i = i.next
        j = i
        while i.next:
            if i.next.val < x:
                t = i.next
                i.next = i.next.next
                t.next = j.next
                j.next = t
                j = j.next
            else:
                i = i.next
        return _head.next