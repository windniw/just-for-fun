"""

link: https://leetcode-cn.com/problems/sequence-reconstruction

problem: 给数组 org，与数组集合seqs，问能否满足 seqs 中的数组均为 org 的子序列，
         且不存在另一个不同的 org' 满足 seqs 中元素也均为其子序列

solution: 拓扑排序。根据 seqs 中每个数组 seq，构建 seq[i] --> seq[i+1] 的图m，若该图的唯一拓扑序为 org，则满题意。  

"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n, visit = len(org), set()
        m, in_edge = {i: set() for i in range(1, n + 1)}, [0] * (n + 1)
        for seq in seqs:
            visit = visit.union(set(seq))
        if visit != set(range(1, n + 1)):
            return False
        for seq in seqs:
            for i in range(len(seq) - 1):
                a, b = seq[i], seq[i + 1]
                if b in m[a]:
                    continue
                in_edge[b] += 1
                m[a].add(b)
        q, res = [], []
        for i in range(1, n + 1):
            if in_edge[i] == 0:
                q.append(i)
        while len(q) == 1:
            k = q.pop()
            res.append(k)
            for x in m[k]:
                in_edge[x] -= 1
                if in_edge[x] == 0:
                    q.append(x)
        return res == org
