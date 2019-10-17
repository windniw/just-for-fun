"""

link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

problem: 要求用原地算法清除升序数组的重复项，使其最多出现两次

solution: 直接扫

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return len(nums)
        i, j = 1, 1
        for j in range(1, len(nums) - 1):
            if nums[j - 1] != nums[j + 1]:
                nums[i] = nums[j]
                i += 1
        nums[i] = nums[-1]
        return i + 1