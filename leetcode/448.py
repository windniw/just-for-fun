"""

link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

problem: 给长度为 n 的数组 nums，nums[i] ∈ [1, n]，求 [1,n]中不在数组的元素，要求时间O(n)，不适用额外空间。

solution: 原地标记，修改nums数组，用取反表示元素存在。

"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for v in nums:
            x = abs(v)
            if nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
        res = []
        for i, x in enumerate(nums):
            if x > 0:
                res.append(i+1)
        return res
