"""

link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

problem: 给序列代表股票每日价格，可反复买入卖出，求最大收益

solution: 扫一遍。

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for k in range(1, len(prices)):
            res += max(0, prices[k] - prices[k-1])
        return res