"""

link: https://leetcode-cn.com/problems/graph-valid-tree

problem: 给图，判断能否构成树

solution: dfs。任挑一个节点开始，检查不成环，且所有节点均已访问到。

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
