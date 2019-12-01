"""

link: https://leetcode.com/problems/sum-root-to-leaf-numbers

problem: 根到其叶子的路径视为一个数字，求其和

solution: dfs

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sum = 0

        def dfs(k: TreeNode, t: int):
            nonlocal sum
            if not k:
                return
            if not k.left and not k.right:
                sum += t * 10 + k.val
            dfs(k.left, t * 10 + k.val)
            dfs(k.right, t * 10 + k.val)

        dfs(root, 0)
        return sum