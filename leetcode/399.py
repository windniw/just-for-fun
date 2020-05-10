"""

link: https://leetcode.com/problems/evaluate-division

problem: 离线解不定方程，给定 a/b=x1 , b/c=x2, 求解 a/c 

solution: 询问较多，用字典预算出所有可能的组合，时间复杂度O(n^2)，将每个结果尝试相乘或相除看能否得到新的组合。

"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        q, v = [], {}
        for i in range(len(equations)):
            t = (equations[i][0], equations[i][1], values[i])
            q.append(t)
        while q:
            k = q.pop()
            t = {}
            v[(k[0], k[1])] = k[2]
            for x in v:
                if x[0] == k[0]:
                    t[(x[1], k[1])] = k[2] / v[x]
                if x[0] == k[1]:
                    t[(k[0], x[1])] = k[2] * v[x]
                if x[1] == k[1]:
                    t[(x[0], k[0])] = v[x] / k[2]
                if x[1] == k[0]:
                    t[(x[0], k[1])] = v[x] * k[2]
            for x in t:
                tt = (x[0], x[1], t[x])
                if (x[0], x[1]) not in v and (x[1], x[0]) not in v:
                    q.append(tt)
        res = []
        for x in queries:
            if (x[0], x[1]) in v:
                res.append(v[(x[0], x[1])])
            elif (x[1], x[0]) in v:
                res.append(1 / v[(x[1], x[0])])
            else:
                res.append(-1.0)
        return res
