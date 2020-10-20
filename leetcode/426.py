"""

link: https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

problem: 二叉平衡树转循环双向链表

solution: 中序遍历插链表。

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        tail = head = Node(0)

        def dfs(k: Node):
            if not k:
                return
            nonlocal tail
            dfs(k.left)
            tail.right = Node(k.val, left=tail)
            tail = tail.right
            dfs(k.right)

        dfs(root)
        tail.right = head.right
        head.right.left = tail

        return head.right
