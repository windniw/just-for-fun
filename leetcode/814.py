"""

link: https://leetcode.cn/problems/binary-tree-pruning/

problem: 移除树中所有节点值为 0 的子树

solution: DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(x: TreeNode) -> int:
            if x is None:
                return 0
            l = dfs(x.left)
            if l == 0:
                x.left = None 
            r = dfs(x.right)
            if r == 0:
                x.right = None 
            return l + r + x.val

        if dfs(root) == 0:
            return None
        return root
