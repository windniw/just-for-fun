"""

link: https://leetcode.com/problems/coin-change

problem: n种无限数量的硬币，问能组成总额amount的最小数量

solution: DP。dp[k] 为总额k的最少数量，dp[k+x] = min(dp[k] + x) x∈coins

solution-fix: 除了自下而上做DP，也可以自上而下做备忘录。

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

# ---
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(maxsize=None)
        def visit(x: int) -> int:
            if not x:
                return 0
            res = float("inf")
            for k in coins:
                if x >= k:
                    res = min(res, visit(x - k))
            return res + 1

        x = visit(amount)
        return -1 if x == float("inf") else x
