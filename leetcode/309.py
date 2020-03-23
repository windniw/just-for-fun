"""

link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

problem: 给序列代表股票每日价格，每次卖出冻结一天不允许操作，不允许重合交易，求最大收益

solution: DP。dp[i][0] / dp[i][1] / dp[i][2] 代表第i天交易后，处于可买入，可卖出，冻结中状态时的最大收益

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
        return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
