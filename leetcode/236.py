"""

link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

problem: 找二叉树的LCA

solution: DFS递归

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def f(k: TreeNode) -> int:
            nonlocal res
            if not k:
                return 0
            cnt = 1 if k == p or k == q else 0
            cnt += f(k.left) + f(k.right)
            if cnt == 2 and not res:
                res = k
            return cnt

        f(root)
        return res