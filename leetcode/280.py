"""

link: https://leetcode-cn.com/problems/wiggle-sort

problem: 将数组整理为 nums[0] <= nums[1] >= nums[2] <= nums[3]... 的形式

solution: 扫一遍。a[i-1] <= a[i] 时，若 a[i] < a[i+1], swap(a[i], a[i+1])，因为此时 a[i-1] <= a[i] < a[i+1]，调整完有
          a[i-1] < a[i+1] > a[i]，满足条件且不对之前扫过的产生影响。同理处理 a[i-1] >= a[i] 的情况。

"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        up = True
        for i in range(1, len(nums)):
            if (up and nums[i] < nums[i - 1]) or (not up and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            up = not up
