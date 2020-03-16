"""

link: https://leetcode.com/problems/range-sum-query-2d-immutable

problem: 离线计算矩阵区间和

solution: 离线计算每个左上角矩阵和，将一个矩形拆分成四个矩形的组合

"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return 0
        return self.dp[row2 + 1][col2 + 1] + self.dp[row1][col1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1]
