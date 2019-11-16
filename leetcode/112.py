"""

link: https://leetcode.com/problems/path-sum

problem: 问树是否存在路径和满足要求

solution: 自顶而下传递搜索

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = False

        def dfs(k: TreeNode, cur: int):
            if not k:
                return
            nonlocal res
            if not k.left and not k.right:
                if k.val + cur == sum:
                    res = True
                return
            dfs(k.left, cur + k.val)
            dfs(k.right, cur + k.val)

        dfs(root, 0)
        return res