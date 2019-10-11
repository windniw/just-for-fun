"""

link: https://leetcode.com/problems/sort-colors

problem: 给定数组只含 0,1,2 三个数字，求只遍历一次，且空间复杂度为O(1)的排序算法

solution: 又名荷兰国旗问题，三个指针扫一遍，尽量将0向前换，1不动，2向后换

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1