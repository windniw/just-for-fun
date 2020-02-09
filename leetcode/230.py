"""

link: https://leetcode.com/problems/kth-smallest-element-in-a-bst

problem: 查找二叉排序树第k小的元素

solution: 转数组返回对应下标

solution-fix: 用栈循环代替递归，找到第k时直接返回，避免遍历整棵树

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []

        def dfs(k: TreeNode):
            if not k:
                return
            dfs(k.left)
            l.append(k.val)
            dfs(k.right)

        dfs(root)
        return l[k-1]
# ---
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        t, s = root, []
        while True:
            while t:
                s.append(t)
                t = t.left
            t = s.pop()
            k -= 1
            if k == 0:
                return t.val
            t = t.right