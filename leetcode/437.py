"""

link: https://leetcode.com/problems/path-sum-iii

problem: 求二叉树上是否存在路径满足和为给定数

solution: 枚举起点的根元素，遍历所有子节点求其和

solution-fix: 维护前缀和的字典。只要记录之前在树的一条路径上，前缀和是否出现过 m[cur_sum] - sum，出现的次数即为路径条数。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def cal(k: TreeNode, s: int) -> int:
            if not k:
                return 0
            s -= k.val
            t = 1 if s == 0 else 0
            return t + cal(k.left, s) + cal(k.right, s)

        if not root:
            return 0
        return cal(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

# ---
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(k: TreeNode, s: int, m: dict) -> int:
            if not k:
                return 0
            cur, t = s + k.val, 0
            t += m[cur - sum] if cur - sum in m else 0
            m[cur] = m[cur] + 1 if cur in m else 1
            t += dfs(k.left, cur, m) + dfs(k.right, cur, m)
            m[cur] -= 1
            return t

        return dfs(root, 0, {0: 1})