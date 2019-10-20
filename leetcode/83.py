"""

link: https://leetcode.com/problems/remove-duplicates-from-sorted-list

problem: 删除链表中的重复项，使每项唯一

solution: 直接扫

"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        while t:
            if t.next and t.next.val == t.val:
                t.next = t.next.next
            else:
                t = t.next
        return head