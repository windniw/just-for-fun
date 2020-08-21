"""

link: https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence

problem: 求二叉树自上而下的最长连续递增长度

solution: 记录当前父节点的长度向下 dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = 0

        def f(k: TreeNode, prev: int, cnt: int):
            nonlocal res
            if not k:
                return
            cnt = cnt + 1 if k.val == prev + 1 else 1
            res = max(res, cnt)
            f(k.left, k.val, cnt)
            f(k.right, k.val, cnt)

        f(root, float("inf"), 0)
        return res
