"""

link: https://leetcode.com/problems/pacific-atlantic-water-flow

problem: 用矩阵代表地面高度，规定只能从高向低走，求所有可达两侧边界的格子

solution: BFS。

"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        q, v = [], set()

        def in_queue(t: tuple):
            q.append(t)
            v.add(t)

        def visit():
            while q:
                t = q.pop()
                i, j = t[0], t[1]
                if i > 0 and matrix[i - 1][j] >= matrix[i][j] and ((i - 1, j) not in v):
                    in_queue((i - 1, j))
                if i < n - 1 and matrix[i + 1][j] >= matrix[i][j] and ((i + 1, j) not in v):
                    in_queue((i + 1, j))
                if j > 0 and matrix[i][j - 1] >= matrix[i][j] and ((i, j - 1) not in v):
                    in_queue((i, j - 1))
                if j < m - 1 and matrix[i][j + 1] >= matrix[i][j] and ((i, j + 1) not in v):
                    in_queue((i, j + 1))

        for i in range(n):
            in_queue((i, 0))
        for i in range(m):
            in_queue((0, i))
        visit()
        v1 = v.copy()

        q, v = [], set()
        for i in range(n):
            in_queue((i, m - 1))
        for i in range(m):
            in_queue((n - 1, i))
        visit()
        return list(v1.intersection(v))
