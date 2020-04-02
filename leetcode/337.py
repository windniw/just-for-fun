"""

link: https://leetcode.com/problems/house-robber-iii

problem: 给二叉树，挑节点，要求选中节点不能相邻，求最大和

solution: 树形DP。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(k: TreeNode) -> (int, int):
            if not k:
                return 0, 0
            rob_left, not_rob_left = dfs(k.left)
            rob_right, not_rob_right = dfs(k.right)
            return not_rob_left + not_rob_right + k.val, max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        
        return max(dfs(root))
