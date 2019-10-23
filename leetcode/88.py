"""

link: https://leetcode.com/problems/merge-sorted-array

problem: 合并两个有序数组

solution: 归并排序

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = [0] * (m + n)
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            nums[k] = nums2[j]
            j += 1
            k += 1
        for i in range(len(nums)):
            nums1[i] = nums[i]