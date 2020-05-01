"""

link: https://leetcode.com/problems/sum-of-left-leaves

problem: 求树的所有左叶子的和。

solution: 递归。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        t = 0
        if root.left and not root.left.left and not root.left.right:
            t = root.left.val
        return t + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

