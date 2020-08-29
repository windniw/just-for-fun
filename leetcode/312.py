"""

link: https://leetcode-cn.com/problems/burst-balloons

problem: 依次移走数组元素，每次移除 nums[i] 时获得 nums[i-1] * nums[i] * nums[i+1] 的分数，假设两侧边界外值均为1，求最高分

solution: DP。dp[i][j] 记录 nums(i, j) 这个开区间内的最高分。状态转移方程有：
          dp[i][j] = max{dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] | k ∈ (i,j)} 
          即，每次假设第 k 个元素是 (i, j) 这个范围内最后一个被移走的元素，则其两侧区间状态互不干扰。

"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for m in range(2, n + 2):
            for i in range(n + 1):
                j = i + m
                if j > n + 1:
                    continue
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n + 1]
