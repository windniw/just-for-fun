"""

link: https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph

problem: 求无向图中连通分量的数量。

solution: 并查集。

"""
class unionSet:
    def __init__(self, n):
        self.data = [i for i in range(n)]

    def join(self, a, b) -> bool:
        m = self.data
        aa, bb = self.find(a), self.find(b)
        if aa == bb:
            return False
        m[aa] = m[bb]
        return True

    def find(self, a) -> int:
        m, k = self.data, a
        while m[k] != k:
            k = m[k]
        while m[a] != k:
            m[a] = k
        return k

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ss = unionSet(n)
        for edge in edges:
            ss.join(edge[0], edge[1])
        res = set()
        for i in range(n):
            res.add(ss.find(i))
        return len(res)
