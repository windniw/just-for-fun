"""

link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array

problem: 返回 target 在 nums 中的区间，不存在时返回 [-1, -1]

solution: 二分

"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target)
        if a == b:
            return [-1, -1]
        else:
            return [a, b - 1]
