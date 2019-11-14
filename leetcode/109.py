"""

link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

problem: 有序链表转平衡树

solution: 转数组，照常

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(x: List[int]) -> TreeNode:
            if len(x) == 0:
                return None
            mid = len(x) >> 1
            k = TreeNode(x[mid])
            k.left = dfs(x[:mid])
            k.right = dfs(x[mid + 1:])
            return k

        l = []
        while head:
            l.append(head.val)
            head = head.next
        return dfs(l)