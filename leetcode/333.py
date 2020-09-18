"""

link: https://leetcode-cn.com/problems/largest-bst-subtree

problem: 求树中最大的二叉排序子树的节点数，注意二叉排序树的左右儿子必须严格小于大于自身，要求时间O(n)

solution: 树形DP。深搜遍历，自底向上更新子树的最小，最大，节点数量，以及是否为合法的二叉排序树。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def dfs(k: TreeNode) -> (bool, int, int, int):
            nonlocal res
            bst, smin, smax, n = True, k.val, k.val, 1
            if k.left:
                is_left_bst, smin, lmax, cnt = dfs(k.left)
                bst &= is_left_bst and lmax < k.val
                n += cnt
            if k.right:
                is_right_bst, rmin, smax, cnt = dfs(k.right)
                bst &= is_right_bst and rmin > k.val
                n += cnt
            if bst:
                res = max(res, n)
                return True, smin, smax, n
            else:
                return False, 0, 0, 0

        dfs(root)
        return res
