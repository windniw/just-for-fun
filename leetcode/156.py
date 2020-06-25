"""

link: https://leetcode-cn.com/problems/binary-tree-upside-down

problem: 翻转二叉树，对于每个右节点，其定为叶子节点，且存在左兄弟；要求翻转完每个节点的右兄弟为其左儿子，父节点为其右儿子

solution: 题意不好理解。递归翻转每个节点即可。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        def f(k: TreeNode):
            if not k or not k.left:
                return k
            l, r = k.left, k.right
            f(k.left), f(k.right)
            l.left, l.right = r, k
            k.left = k.right = None

        k = root
        while k and k.left:
            k = k.left
        f(root)
        return k