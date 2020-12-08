"""

link: https://leetcode-cn.com/problems/encode-n-ary-tree-to-binary-tree

problem: 将多叉树转换为二叉树，并转回

solution: 左节点为父节点的子节点，右节点为父节点的兄弟节点

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        def dfs(k: Node) -> TreeNode:
            kt = TreeNode(k.val)
            for i, c in enumerate(k.children):
                t = dfs(c)
                if i == 0:
                    kt.left = t
                else:
                    pre.right = t
                pre = t
            return kt

        return dfs(root)

    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        a = Node(0, [])

        def dfs(k: TreeNode, father: Node):
            if not k:
                return
            t = Node(k.val, [])
            father.children.append(t)
            dfs(k.right, father)
            dfs(k.left, t)

        dfs(data, a)
        return a.children[0]
