"""

link: https://leetcode-cn.com/problems/count-univalue-subtrees

problem: 统计二叉树中，所有子节点值均一致的子树数量。

solution: dfs。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def dfs(k: TreeNode) -> (int, bool):
            if not k:
                return 0, True
            n_left, is_left = dfs(k.left)
            n_right, is_right = dfs(k.right)
            n, res = n_left + n_right, is_left and (k.left is None or k.val == k.left.val) and is_right and (
                    k.right is None or k.val == k.right.val)
            if res:
                n += 1
            return n, res

        res, _ = dfs(root)
        return res
