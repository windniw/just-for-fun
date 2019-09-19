"""

link: https://leetcode.com/problems/spiral-matrix

problem: 螺旋遍历矩阵

solution: 依次遍历(0,0)(1,1)...为左上顶点的矩形边

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        n, m, res = len(matrix), len(matrix[0]), []

        def ring(i):
            for k in range(i, m - i):
                res.append(matrix[i][k])
            if m - 1 - i >= 0:
                for k in range(i + 1, n - 1 - i):
                    res.append(matrix[k][m - 1 - i])
            if n - 1 - i >= 0 and n - 1 - i > i:
                for k in range(m - i - 1, i - 1, -1):
                    res.append(matrix[n - 1 - i][k])
            if m - 1 - i > i:
                for k in range(n - 2 - i, i, -1):
                    res.append(matrix[k][i])

        for k in range(0, min((n + 1) // 2, (m + 1) // 2)):
            ring(k)

        return res
