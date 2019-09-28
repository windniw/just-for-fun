"""

link: https://leetcode.com/problems/minimum-path-sum

problem: 求n*m棋盘从左上角到右下角的路线，要求路线上格子之和最小

solution: DP, 定义dp[i][j]为走到grid[i][j]的最小值
dp[0][i] = sum(grid[0][0~i])
dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
顺便压缩个空间到O(n)即可
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [grid[0][i] for i in range(m)]
        for i in range(1, m):
            dp[i] += dp[i - 1]

        for i in range(1, n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[m - 1]