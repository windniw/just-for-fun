"""

link: https://leetcode.com/problems/binary-tree-inorder-traversal

problem: 求树的中序遍历

solution: DFS

"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(x: TreeNode):
            if x is None: return
            dfs(x.left)
            res.append(x.val)
            dfs(x.right)
        dfs(root)
        return res
