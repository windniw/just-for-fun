"""

link: https://leetcode.com/problems/linked-list-random-node

problem: 对链表随机返回节点，要求 O(1) 级别的空间复杂度

solution: 统计长度，随机位置

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