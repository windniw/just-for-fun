"""

link: https://leetcode.com/problems/path-sum-ii

problem: 求树所有路径和满足要求的路径

solution: 自顶而下传递搜索

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(k: TreeNode, cur: int, path: List[int]):
            if not k:
                return
            tp = path.copy()
            tp.append(k.val)
            nonlocal res
            if not k.left and not k.right:
                if k.val + cur == sum:
                    res.append(tp)
                return
            dfs(k.left, cur + k.val, tp)
            dfs(k.right, cur + k.val, tp)

        dfs(root, 0, [])
        return res   