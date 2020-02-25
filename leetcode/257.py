"""

link: https://leetcode.com/problems/binary-tree-paths

problem: 输出树所有根到叶子的路径

solution: DFS遍历

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []

        def f(k: TreeNode, t: str) -> bool:
            if not k:
                return True
            if not k.left and not k.right:
                res.append(t + str(k.val))
            f(k.left, t + str(k.val) + "->")
            f(k.right, t + str(k.val) + "->")

        f(root, "")
        return res