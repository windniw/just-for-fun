"""

link: https://leetcode.com/problems/path-sum-iii

problem: 求二叉树上是否存在路径满足和为给定数

solution: 枚举起点的根元素，遍历所有子节点求其和

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def cal(k: TreeNode, s: int) -> int:
            if not k:
                return 0
            s -= k.val
            t = 1 if s == 0 else 0
            return t + cal(k.left, s) + cal(k.right, s)

        if not root:
            return 0
        return cal(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
