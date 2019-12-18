"""

link: https://leetcode.com/problems/linked-list-cycle-ii

problem: 判断链表中是否存在环，输出环的起始指针，要求空间O(1)

solution: 快慢指针。将过程分为三部分，记图非环路径长度为 F, 环长度为 C
          <F> -- <F-1> -- <F-2> -- <F-3> -- ... -- <0> -- <1> -- <2>
                                                    |             |
                                                   <5> -- <4> -- <3>
          当存在环时，肯定存在以下部分：
          1. slow 走到 0, fast 走到 h，有 F ≡ h (mod C)
          2. 继续，fast 与 slow 向前直至重叠点，重叠点必为 C-h (slow 走的长度为 c-h，fast 为 2*(c-h))
          3. 继续。令 t 重新从 head 出发，slow 继续向前，两指针必相会于0。
               (C - h + F) mod C
             = C mod C + (F - h) mod C
             = C mod C
             = 0
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        t = head
        while t != slow:
            t, slow = t.next, slow.next
        return t