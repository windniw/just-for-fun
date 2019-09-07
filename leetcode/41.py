"""

link: https://leetcode.com/problems/first-missing-positive

problem: 求nums中最小的未出现正整数，要求时间复杂度O(n), 空间复杂度O(1)

solution: 桶排序，忽略掉 <= 0 || >= len(nums) 的值，原地交换解决空间复杂度的问题即可

"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
