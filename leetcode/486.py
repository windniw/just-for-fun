"""

link: https://leetcode-cn.com/problems/predict-the-winner

problem: 给定数组 nums，A,B两人轮流从数组两侧拿数字至空，数字和最大者胜，问A是否有必胜策略。

solution: 记忆化搜索。时间复杂度 O(2^n)

solution-fix: DP。记dp[i][j]为当先手角色面临nums[i:j+1]时，其能拿到的最好的分数差。由小区间向大区间来扩容这个状态，
              显然，当 i==j 时，dp[i][j] = nums[i]，即直接拿走剩下的唯一元素；当 i!=j 时，dp[i][j] = 
              max(-dp[i+1][j]+nums[i], -dp[i][j-1]+nums[j])。时间复杂度 O(n^2)。

"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(maxsize=None)
        def f(i, j, a, b, first):
            if i == j:
                return (first and a + nums[i] >= b) or a >= nums[i] + b
            if first:
                return f(i + 1, j, a + nums[i], b, False) or f(i, j - 1, a + nums[j], b, False)
            else:
                return f(i + 1, j, a, b + nums[i], True) and f(i, j - 1, a, b + nums[j], True)

        return f(0, len(nums) - 1, 0, 0, True)

# ---
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if not nums:
            return True
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j][i] = nums[i]
                else:
                    dp[j][i] = max(-dp[j + 1][i] + nums[j], -dp[j][i - 1] + nums[i])
        return dp[0][n - 1] >= 0
