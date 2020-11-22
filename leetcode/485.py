"""

link: https://leetcode-cn.com/problems/max-consecutive-ones

problem: 求 01 数组中最长的连续 1 数量

solution: 扫描。

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, p, n = 0, -1, len(nums)
        for i in range(n):
            if nums[i] == 0:
                p = i
            else:
                res = max(res, i - p)
        return res
