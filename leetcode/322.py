"""

link: https://leetcode.com/problems/coin-change

problem: n种无限数量的硬币，问能组成总额amount的最小数量

solution: DP。dp[k] 为总额k的最少数量，dp[k+x] = min(dp[k] + x) x∈coins

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        coins.sort()
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for x in range(amount - coins[0] + 1):
            for k in coins:
                if x + k > amount:
                    break
                dp[x + k] = min(dp[x + k], dp[x] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
