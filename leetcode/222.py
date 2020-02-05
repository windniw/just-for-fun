"""

link: https://leetcode.com/problems/count-complete-tree-nodes

problem: 计算完全二叉树结点数量

solution: DFS

solution-fix: 考虑完全二叉树的特殊性，如果是满二叉树，则其节点数量为 2^(d-1), d为高度；
              而完全二叉树只可能存在最下层不满的情况与这个值有偏差，拆分计算为 d-1 的满二叉树，
              以及最下层的二分检查，时间复杂从 O(2^d) 降低为 O(d^2)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# ---
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        k, depth = root, 0
        while k:
            k = k.left
            depth += 1

        def exist(k: TreeNode, num: int, d: int) -> bool:
            if not k:
                return False
            if d == depth:
                return True
            return exist(k.right, num, d + 1) if ((1 << (depth - 1 - d)) & num) != 0 else exist(k.left, num, d + 1)

        l, r, res = 0, (1 << (depth - 1)) - 1, 0
        while l <= r:
            mid = (l + r) >> 1
            if exist(root, mid, 1):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return (1 << (depth - 1)) + res
