"""

link: https://leetcode.com/problems/intersection-of-two-linked-lists

problem: 两个链表尾部重合，求相交点。要求时间 O(n)，空间 O(1)。

solution: 双指针。遍历A、B，求其长度差，先抹平差值再重新遍历，指针即会合于相交点。

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ta, tb, la, lb = headA, headB, 0, 0
        while ta:
            ta = ta.next
            la += 1
        while tb:
            tb = tb.next
            lb += 1
        if ta != tb:
            return None
        if la > lb:
            ta, tb = headA, headB
        else:
            ta, tb = headB, headA
        for _ in range(abs(la - lb)):
            ta = ta.next
        while ta != tb:
            ta, tb = ta.next, tb.next
        return ta
