"""

link: https://leetcode.com/problems/symmetric-tree

problem: 判断树是否镜像对称

solution: 翻转递归检查

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(t1: TreeNode, t2: TreeNode):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and compare(t1.left, t2.right) and compare(t1.right, t2.left)
        return not root or compare(root.left, root.right)