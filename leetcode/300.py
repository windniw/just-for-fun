"""

link: https://leetcode-cn.com/problems/longest-increasing-subsequence

problem: 求最长上升子序列(LIS)长度

solution: dp。dp[i] 为 nums[:i] 的LIS长度, dp[j] = max{dp[i] + 1 | i < j && nums[i] < nums[j]}。时间复杂度 O(n^2)

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if nums[i] < nums[j] and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
        return max(dp)
