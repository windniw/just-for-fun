"""

link: https://leetcode-cn.com/problems/graph-valid-tree

problem: 给图，判断能否构成树

solution: dfs。任挑一个节点开始，检查不成环，且所有节点均已访问到。

solution: 并查集 + 按序合并 + 路径压缩。合并路径两端，判断是否成环，且仅有一个连通分量。

"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        es = collections.defaultdict(list)
        for edge in edges:
            es[edge[0]].append(edge[1])
            es[edge[1]].append(edge[0])
        visit = [False for _ in range(n)]

        def dfs(k: int, parent: int) -> bool:
            visit[k] = True
            for x in es[k]:
                if x == parent:
                    continue
                if visit[x]:
                    return False
                if not dfs(x, k):
                    return False
            return True

        return dfs(0, -1) and all(visit)

# ---
class Solution:
    class unionSet:
        def __init__(self, n):
            self.data = [i for i in range(n)]
            self.rank = [0 for i in range(n)]

        def join(self, a, b):
            m, r = self.data, self.rank
            aa, bb = self.find(a), self.find(b)
            if aa != bb:
                if r[aa] > r[bb]:
                    m[bb] = m[aa]
                elif r[bb] > r[aa]:
                    m[aa] = m[bb]
                else:
                    m[aa] = m[bb]
                    r[aa] += 1

        def find(self, a) -> int:
            m, k = self.data, a
            while m[k] != k:
                k = m[k]
            while m[a] != k:
                m[a] = k
            self.rank[k] = 2
            return k

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        us = self.unionSet(n)
        for edge in edges:
            if us.find(edge[0]) == us.find(edge[1]):
                return False
            us.join(edge[0], edge[1])
        return all([us.find(i) == us.find(0) for i in range(1, n)])
