"""

link: https://leetcode.com/problems/binary-tree-preorder-traversal

problem: 先序遍历，要求循环不能用递归

solution: 栈

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            x = stack.pop()
            res.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        return res
