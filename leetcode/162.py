"""

link: https://leetcode.com/problems/find-peak-element

problem: 求数组峰值下标，要求时间 O(logn)

solution: 二分。

"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
