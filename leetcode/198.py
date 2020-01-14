"""

link: https://leetcode.com/problems/house-robber

problem: 给数组nums，挑数字，求最大和，相邻数字仅可选其中一个

solution: DP。dp[i][0]表示选到第i位时，不选它可得到的最大值，dp[i][1]表示选的最大值。

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        dp = [[0, 0] for _ in range(l)]
        dp[0][1] = nums[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[l - 1][0], dp[l - 1][1])