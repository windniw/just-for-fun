"""

link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node

problem: 对完美二叉树的每个节点补充 next 值，定义为在其右侧的节点，要求用常数空间或递归

solution: 递归。对每个子树，其根节点只需关联左右儿子，及通过next，关联右儿子与兄弟的左儿子。

solution-fix: 常数空间循环。利用next指针，按层向下做BFS。

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

# ---
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = root
        while level:
            k = level
            level = level.left
            while k:
                if k.left:
                    k.left.next = k.right
                    if k.next:
                        k.right.next = k.next.left
                k = k.next
        return root