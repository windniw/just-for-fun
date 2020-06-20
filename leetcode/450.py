"""

link: https://leetcode.com/problems/delete-node-in-a-bst

problem: 实现avl树的删除

solution: 递归。找到key值对应的节点，用左子树的最大值或右子树的最小值替换该节点的key值，递归移除对应的子树的替换值。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def left_max(k: TreeNode) -> int:
            while k and k.right:
                k = k.right
            return k.val

        def right_min(k: TreeNode) -> int:
            while k and k.left:
                k = k.left
            return k.val

        if not root or (root.val == key and not root.left and not root.right):
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left:
                x = left_max(root.left)
                root.val = x
                root.left = self.deleteNode(root.left, x)
            elif root.right:
                x = right_min(root.right)
                root.val = x
                root.right = self.deleteNode(root.right, x)
        return root
