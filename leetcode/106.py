"""

link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

problem: 给中序，后序，还原树

solution: 利用后序末值定根，中序划分左右的性质，递归划分子树的范围

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        k = TreeNode(postorder[-1])
        left_num = inorder.index(k.val)
        k.left = self.buildTree(inorder[:left_num], postorder[:left_num])
        k.right = self.buildTree(inorder[left_num + 1:], postorder[left_num:-1])
        return k