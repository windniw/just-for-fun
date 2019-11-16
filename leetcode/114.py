"""

link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list

problem: 原地按先序遍历展开树

solution: 记录全局遍历值，向右子树接节点，清空左子树

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = TreeNode(0)

        def dfs(k: TreeNode):
            if not k:
                return
            nonlocal cur
            kr = k.right
            cur.right = k
            cur.left = None
            cur = k
            dfs(k.left)
            dfs(kr)

        dfs(root)
        return cur.right