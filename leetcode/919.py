"""

link: https://leetcode.cn/problems/complete-binary-tree-inserter/

problem: 维护完全二叉树

solution: 记录树节点数量，0左1右，确定待插入的 num 值，即可根据其二进制找到具体位置
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        def dfs(x: TreeNode):
            if x is None:
                return 0
            return dfs(x.left) + dfs(x.right) + 1
        self.n = dfs(root)
        self.root = TreeNode(-1)
        self.root.left = root

    def insert(self, val: int) -> int:
        self.n += 1
        x = self.root
        for i in bin(self.n >> 1)[2:]:
            if i == "0":
                x = x.left
            else:
                x = x.right
        if self.n & 1 == 0:
            x.left = TreeNode(val)
        else:
            x.right = TreeNode(val)
        return x

    def get_root(self) -> TreeNode:
        return self.root.left

