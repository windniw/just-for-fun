"""

link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

problem: 找二叉搜索树的LCA

solution: 根据二叉搜索树特性，其LCA一定满足 p.val <= lca.val <= q.val，递归即可

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root