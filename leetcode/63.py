"""

link: https://leetcode.com/problems/unique-paths-ii

problem: 求n*m棋盘从左上角到右下角的路线数，规定每次只能往右或下走一步，存在障碍格子不能经过

solution: DP。
dp[0][0] = obstacleGrid[0][0] == 0 ? 1 : 0
dp[i][j] = obstacleGrid[0][0] == 0 ? dp[i-1][j] + dp[j-1][i] : 0 
顺便压缩个空间到O(n)即可
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(m)]
        dp[0] = 1
        for i in range(n):
            dp[0] = dp[0] if obstacleGrid[i][0] != 1 else 0
            for j in range(1, m):
                dp[j] = dp[j] + dp[j - 1] if obstacleGrid[i][j] != 1 else 0
            debug(dp)
        return dp[m - 1]
