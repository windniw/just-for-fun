"""

link: https://leetcode-cn.com/problems/diagonal-traverse

problem: 按斜对角线循环遍历

solution: 模拟。循环斜向下遍历，碰边界后反向。

"""
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        i, j, n, m, res = 0, 0, len(matrix), len(matrix[0]), []
        ii, jj = -1, 1
        while True:
            res.append(matrix[i][j])
            if i == n - 1 and j == m - 1:
                return res
            if 0 <= i + ii < n and 0 <= j + jj < m:
                i += ii
                j += jj
                continue
            if i + ii < 0 and j != m - 1:
                j += 1
            elif j + jj >= m:
                i += 1
            elif j + jj < 0 and i != n - 1:
                i += 1
            elif i + ii >= n:
                j += 1
            ii = -ii
            jj = -jj
