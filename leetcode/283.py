"""

link: https://leetcode.com/problems/move-zeroes

problem: 将数组非零值前移，保持顺序不变，要求空间O(1)

solution: 双指针

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j, n = 0, 0, len(nums)
        while i < n and j < n:
            if nums[i] == 0:
                i += 1
                continue
            while j < n and nums[j] != 0:
                j += 1
            if j < i:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
