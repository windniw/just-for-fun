"""

link: https://leetcode.com/problems/n-ary-tree-level-order-traversal

problem: 按层遍历多叉树

solution: BFS

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res, q, q_next = [], [root], []
        while q:
            cur = []
            for k in q:
                cur.append(k.val)
                if k.children:
                    q_next.extend(k.children)
            res.append(cur)
            q = q_next
            q_next = []
        return res
