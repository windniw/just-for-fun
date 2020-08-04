"""

link: https://leetcode-cn.com/problems/closest-binary-search-tree-value

problem: 求二叉排序树中与给定浮点数最接近的值

solution: 两次二分。搜索该浮点数在排序树中的上下最接近值，比较。

solution-fix: 搜索路径是一致的，没必要遍历两次。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_val, max_val = float("-inf"), float("inf")

        def f_min(k: TreeNode):
            if not k:
                return
            nonlocal min_val
            if target >= k.val > min_val:
                min_val = k.val
            f_min(k.left if k.val > target else k.right)

        def f_max(k: TreeNode):
            if not k:
                return
            nonlocal max_val
            if target <= k.val < max_val:
                max_val = k.val
            f_max(k.left if k.val > target else k.right)

        f_min(root)
        f_max(root)
        return max_val if target - min_val > max_val - target else min_val

# ---
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float("inf")

        def f(k: TreeNode):
            if not k:
                return
            nonlocal res
            if math.fabs(res - target) > math.fabs(k.val - target):
                res = k.val
            f(k.left if k.val > target else k.right)

        f(root)
        return res

