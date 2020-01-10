"""

link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

problem: 升序数组从中间某点断开后重拼接，求最小值，数组中元素可能相等

solution: 二分。与 153 相比，重复元素唯一可能的影响的数组前后一致，向前移l以排除此场景即可。

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == nums[r]:
            l += 1
        if nums[r] >= nums[l]:
            return nums[l]
        base = l
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= nums[base]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
