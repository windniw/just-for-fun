"""

link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

problem: 给序列代表股票每日价格，最多允许买卖两次，不允许重合交易，求最大收益

solution: 两次交易不允许重合，预先处理好 dp[0,k], dp[k+1, n-1]的最大收益，枚举断点即可

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        left_dp, right_dp = [0 for i in range(n)], [0 for i in range(n)]
        k = prices[0]
        for i in range(1, n):
            left_dp[i] = max(left_dp[i - 1], prices[i] - k)
            if prices[i] < k:
                k = prices[i]
        k = prices[n - 1]
        for i in reversed(range(n - 1)):
            right_dp[i] = max(right_dp[i + 1], k - prices[i])
            if prices[i] > k:
                k = prices[i]
        res = left_dp[n - 1]
        for i in range(n - 1):
            res = max(res, left_dp[i] + right_dp[i + 1])
        return res