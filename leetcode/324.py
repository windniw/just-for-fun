"""

link: https://leetcode-cn.com/problems/wiggle-sort-ii

problem: 将数组重整为 nums[0] < nums[1] > nums[2] < nums[3]... 的格式，要求时间O(n) 或 空间O(1)

solution: 排序后从中间断开，记排序完为t，将 t[0:n//2+2], t[n//2+2:n] 分别翻转后合并拼接即满足条件。时间O(nlogn)，空间O(n)

"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        t, n = nums.copy(), len(nums)
        t.sort()
        for i in range(n // 2):
            nums[2 * i] = t[n // 2 + (n & 1) - 1 - i]
            nums[2 * i + 1] = t[n - 1 - i]
        if n & 1:
            nums[-1] = t[0]
