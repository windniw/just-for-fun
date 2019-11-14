"""

link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

problem: 给先序，中序，还原树

solution: 利用先序定根，中序划分左右的性质，递归划分子树的范围

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        k = TreeNode(preorder[0])
        left_num = inorder.index(k.val)
        k.left = self.buildTree(preorder[1:left_num + 1], inorder[:left_num])
        k.right = self.buildTree(preorder[left_num + 1:], inorder[left_num + 1:])
        return k
