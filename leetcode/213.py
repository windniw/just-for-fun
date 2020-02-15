"""

link: https://leetcode.com/problems/house-robber-ii

problem: 给数组nums，挑数字，求最大和，相邻数字仅可选其中一个，首尾成环视为相邻

solution: DP。类198，dp[i][0]表示选到第i位时，不选它可得到的最大值，dp[i][1]表示选的最大值。
          做两次dp，分别枚举首位选或者不选的情况。

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(nums: List[int]) -> int:
            n = len(nums)
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = nums[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + nums[i]
            return max(dp[n - 1][0], dp[n - 1][1])

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(f(nums[:-1]), f(nums[1:]))
