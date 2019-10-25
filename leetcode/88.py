"""

link: https://leetcode.com/problems/merge-sorted-array

problem: 合并两个有序数组

solution: 归并排序

solution: 题目特殊性，可以原地排序，因为剩余空间在nums1的后半段，所以倒序归并，直接使用nums1的空间可以省去O(n)的空间开销

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

# --- 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, n + m - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]
