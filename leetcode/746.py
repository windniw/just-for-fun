"""

link: https://leetcode-cn.com/problems/min-cost-climbing-stairs

problem: 跳楼梯。

solution: DP。 dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1], dp[i])

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        f = [float("inf") for _ in range(n + 2)]
        f[0] = f[1] = 0
        for i in range(n):
            f[i + 1] = min(f[i + 1], f[i] + cost[i])
            f[i + 2] = min(f[i + 2], f[i] + cost[i])
        return int(f[n])
