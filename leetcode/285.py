"""

link: https://leetcode-cn.com/problems/inorder-successor-in-bst

problem: 查找排序树中某元素的下一个节点

solution: 二叉排序树中元素的下一个节点，要么是其父节点，要么是其右儿子的最底左儿子。先二分找到该元素后检查。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res, found = None, False

        def dfs(k: TreeNode):
            nonlocal res, found
            if not k:
                return
            if k.val == p.val:
                found = True
                if k.right:
                    res = k.right
                    while res.left:
                        res = res.left
                    return
            else:
                dfs(k.left) if p.val < k.val else dfs(k.right)
            if found and res is None and p.val < k.val:
                res = k

        dfs(root)
        return res
