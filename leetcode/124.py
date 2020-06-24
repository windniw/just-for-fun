"""

link: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum

problem: 非空二叉树，求路径的最大值，节点可能为负数

solution: 树型DP。自底向上记录以节点k为端点的路径的最大值。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def f(k: TreeNode) -> int:
            nonlocal res
            if not k:
                return 0
            l, r = f(k.left), f(k.right)
            t = max(k.val, k.val + l, k.val + r)
            res = max(res, t, k.val + l + r)
            return t

        f(root)
        return res
