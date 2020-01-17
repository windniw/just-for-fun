"""

link: https://leetcode.com/problems/binary-tree-right-side-view

problem: 输出二叉树的右视图

solution: 递归遍历记录高度的最后一个值。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(k: TreeNode, height: int):
            if not k:
                return
            if len(res) <= height:
                res.append(k.val)
            else:
                res[height] = k.val
            dfs(k.left, height + 1)
            dfs(k.right, height + 1)

        dfs(root, 0)
        return res