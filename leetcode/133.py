"""

link: https://leetcode.com/problems/clone-graph

problem: 深拷贝图

solution: BFS + 字典

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {node: Node(node.val, [])}
        queue = [node]
        while len(queue) != 0:
            t = queue[0]
            queue = queue[1:]
            tt = clone[t]
            for x in t.neighbors:
                if x not in clone:
                    clone[x] = Node(x.val, [])
                    queue.append(x)
                tt.neighbors.append(clone[x])
        return clone[node]