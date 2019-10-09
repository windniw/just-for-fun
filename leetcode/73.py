"""

link: https://leetcode.com/problems/set-matrix-zeroes

problem: 给定矩阵，若 matrix[i][j] == 0 则 matrix[k][...] = matrix[...][k] = 0。要求时间复杂度O(n*m), 空间复杂度O(1)

solution: 用矩阵的第0行 第0列来记录信息，若该位置零代表最后扫描时需要将该行或该列全部置零
matrix[0][0] 同时表达了第0行和第0列，有冲突，拆分成两个变量保存

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        n, m = len(matrix), len(matrix[0])
        zero_row = zero_col = tmp = matrix[0][0]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        zero_row = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        zero_col = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zero_row == 0:
            for i in range(m): matrix[0][i] = 0
        if zero_col == 0:
            for j in range(n): matrix[j][0] = 0