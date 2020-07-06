"""

link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv

problem: 给定数组代表某支股票每日的价格，限定买卖k次，必须卖完才能买，求最大收益。

solution: DP。股票系列的最后一题。dp[n][k][0] 代表第n天结束，还可以交易k次时，手中没有股票，此时的收益; dp[n][k][1] 代表手上有股票时的收益。
          定义卖出时股票时，交易次数才被消耗掉，显然有：
            // 空仓结束时的最优抉择为：卖出，不操作
            dp[i][j][0] = max(dp[i - 1][j + 1][1] + prices[i], dp[i - 1][j][0])
            // 满仓结束时的最优抉择为：买入，不操作
            dp[i][j][1] = max(dp[i - 1][j][0] - prices[i], dp[i - 1][j][1])
          时限卡的太死，对于 k > n // 2 的情况必须直接优化成 O(n) 的做法不然会超时，其实这说明样例有问题，否则原数据构造一个 k = n // 2 就能完全卡死

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        if k > n // 2:
            dp = [[0, 0] for _ in range(n)]
            dp[0][0], dp[0][1] = 0, -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
                dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            return dp[n - 1][0]
        else:
            # 0 空仓 1 持有
            dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
            for i in range(n):
                dp[i][k][1] = -prices[i]
            for i in range(k + 1):
                dp[0][i][1] = -prices[0]
            for i in range(1, n):
                for j in reversed(range(k + 1)):
                    if j == k:
                        dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j][1])
                    else:
                        dp[i][j][0] = max(dp[i - 1][j + 1][1] + prices[i], dp[i - 1][j][0])
                        dp[i][j][1] = max(dp[i - 1][j][0] - prices[i], dp[i - 1][j][1])
            return dp[n - 1][0][0]
