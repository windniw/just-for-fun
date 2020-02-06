"""

link: https://leetcode.com/problems/kth-smallest-element-in-a-bst

problem: 查找二叉排序树第k小的元素

solution: 转数组返回对应下标

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []

        def dfs(k: TreeNode):
            if not k:
                return
            dfs(k.left)
            l.append(k.val)
            dfs(k.right)

        dfs(root)
        return l[k-1]
