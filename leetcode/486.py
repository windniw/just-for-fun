"""

link: https://leetcode-cn.com/problems/predict-the-winner

problem: 给定数组 nums，A,B两人轮流从数组两侧拿数字至空，数字和最大者胜，问A是否有必胜策略。

solution: 记忆化搜索。时间复杂度 O(2^n)

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
