"""

link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

problem: 对二叉树的每个节点补充 next 值，定义为在其右侧的节点，要求用常数空间或递归

solution: 常数空间循环。利用next指针，按层向下做BFS。

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
        level = root
        while level:
            k, pre = level, None
            level = None
            while k:
                if k.left:
                    if pre:
                        pre.next = k.left
                    else:
                        level = k.left
                    pre = k.left
                if k.right:
                    if pre:
                        pre.next = k.right
                    else:
                        level = k.right
                    pre = k.right
                k = k.next
        return root