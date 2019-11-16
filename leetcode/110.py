"""

link: https://leetcode.com/problems/balanced-binary-tree

problem: 判断树是否平衡

solution: 递归求子树高度

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dep(k: TreeNode) -> (bool, int):
            if not k: return True, 0
            s1, ld = dep(k.left)
            s2, rd = dep(k.right)
            return s1 and s2 and abs(ld - rd) <= 1, max(ld, rd) + 1

        return dep(root)[0]