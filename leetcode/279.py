"""

link: https://leetcode.com/problems/perfect-squares

problem: 将给定数字 n 拆分成若干个完全平方数之和，求最小数字数

solution: DP。dp[n] = max(dp[n], dp[n-x*x] + 1)

"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n + 1)]
        for x in range(n + 1):
            t = 0
            while t * t <= x:
                dp[x] = min(dp[x], dp[x - t * t] + 1)
                t += 1
        return dp[n]
