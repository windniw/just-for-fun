"""

link: https://leetcode.com/problems/maximal-square

problem: 求矩阵中最大的全是1的正方形面积

solution: DP。dp[i][j]表示以matrix[i][j]为右下角的最大正方形边长，有:
          dp[i][j] = matrix[i][j] == 1 ? min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 : 0

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                    res = max(res, dp[i][j])
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                res = max(res, dp[i][j])
        return res * res