"""

link: https://leetcode.com/problems/linked-list-random-node

problem: 对链表随机返回节点，要求 O(1) 级别的空间复杂度

solution: 统计长度，随机位置

solution-fix: 仅遍历一次，对当前第i个元素，有 1/i 的机率保留作为返回结果。需要多次随机，但只需要一次遍历。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.l = 0
        self.head, t = head, head
        while t:
            self.l += 1
            t = t.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        t = random.randint(0, self.l - 1)
        k = self.head
        while t:
            k = k.next
            t -= 1
        return k.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# --- 
class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        k = self.head
        res, n = k.val, 0
        while k:
            n += 1
            if random.randint(1, n) == n:
                res = k.val
            k = k.next
        return res

