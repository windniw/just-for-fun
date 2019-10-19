"""

link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

problem: 删除链表中的重复项，注意是若某项重复，则所有该项都需要移除

solution: 非原地算法，扫一遍跳过所有 t.val == t.next.val 的项

"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = ListNode(0)
        h = t
        while head:
            if head.next and head.next.val == head.val:
                cur = head
                while head and head.val == cur.val:
                    head = head.next
                continue
            t.next = ListNode(head.val)
            t = t.next
            head = head.next
        return h.next
