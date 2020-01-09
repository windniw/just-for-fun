"""

link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

problem: 升序数组从中间某点断开后重拼接，求最小值

solution: 二分, 以 nums[0] 为标准，判断是前段还是后段

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
