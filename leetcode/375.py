"""

link: https://leetcode.com/problems/guess-number-higher-or-lower-ii

problem: 给范围猜数，每次猜消耗与猜测数字等量的金钱，求最坏情况下的消耗

solution: DP。dp[i][j] 代表范围 [i,j] 的最大消耗，枚举起点，终点，猜测点，时间O(n^3), 空间O(n^2)

solution-fix: 枚举猜测点是只需要从中点枚举，因为若落在中点左侧，其消耗一定大于等于中点，可以省掉一半的时间开销

"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 0
        for i in range(1, n + 1):
            for j in reversed(range(1, i)):
                for k in range(j, i + 1):
                    t = k
                    t_left = dp[j][k - 1] if k - 1 >= j else 0
                    t_right = dp[k + 1][i] if i >= k + 1 else 0
                    t += max(t_left, t_right)
                    dp[j][i] = min(dp[j][i], t)
        return dp[1][n]

# ---
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 0
        for i in range(1, n + 1):
            for j in reversed(range(1, i)):
                for k in range((j + i) >> 1, i + 1):
                    t = k
                    t_left = dp[j][k - 1] if k - 1 >= j else 0
                    t_right = dp[k + 1][i] if i >= k + 1 else 0
                    t += max(t_left, t_right)
                    dp[j][i] = min(dp[j][i], t)
        return dp[1][n]
