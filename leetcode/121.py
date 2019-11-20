"""

link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

problem: 找序列最大递增值

solution: 扫一遍。

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, res = prices[0], 0
        for k in range(1, len(prices)):
            if prices[k] < buy:
                buy = prices[k]
            else:
                res = max(res, prices[k] - buy)
        return res