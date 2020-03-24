"""

link: https://leetcode.com/problems/minimum-height-trees

problem: 在无向图中选取一点使其到所有节点的总路径和最短，求所有满足条件的点

solution: 拓扑序。最后出队的一批节点，由图的最外围向内一步步收缩，最后的集合即为结果

"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if not n or not edges:
            return []
        m = collections.defaultdict(list)
        degree = [0 for _ in range(n)]
        q, qq = [], []
        for x in edges:
            m[x[0]].append(x[1])
            m[x[1]].append(x[0])
            degree[x[0]] += 1
            degree[x[1]] += 1

        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        out = 0
        while True:
            if out + len(q) == n:
                return q
            out += len(q)
            while q:
                x = q.pop()
                for d in m[x]:
                    degree[d] -= 1
                    if degree[d] == 1:
                        qq.append(d)
            q = qq
            qq = []