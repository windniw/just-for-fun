"""

link: https://leetcode-cn.com/problems/number-of-islands-ii

problem: 初始为 m*n 的全0图，做k次操作，每次将图的某个节点置为1，求每次操作完图中有几个1的块，要求时间复杂为O(k*logmn)

solution: 并查集 + 路径压缩。每次插入后检查上下左右是否可合并。

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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def f(x, y):
            return x * n + y

        graph, res, us, cnt = [[0 for _ in range(n)] for _ in range(m)], [], unionSet(n * m), 0
        for item in positions:
            x, y, k = item[0], item[1], f(item[0], item[1])
            if graph[x][y] == 1:
                res.append(cnt)
                continue
            graph[x][y] = 1
            cnt += 1
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x + ii, y + jj
                if 0 <= i < m and 0 <= j < n and graph[i][j] == 1:
                    if us.join(f(i, j), k):
                        cnt -= 1
            res.append(cnt)
        return res
