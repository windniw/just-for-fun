"""

link: https://leetcode.com/problems/minimum-depth-of-binary-tree

problem: 求树根到叶子的最小距离

solution: 递归求子树的最小距离

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        res = float("inf")
        if root.left:
            res = min(self.minDepth(root.left) + 1, res)
        if root.right:
            res = min(self.minDepth(root.right) + 1, res)
        return res