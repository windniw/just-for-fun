"""

link: https://leetcode.com/problems/wiggle-subsequence

problem: 若序列元素满足 l[0] < l[1] > l[2] ... 或 l[0] > l[1] < l[2] ... 定义其为摇摆序列，求给定数组的最长摇摆子序列，时间复杂度要求O(n)

solution: 贪心。扫一遍，对非严格上升或下降序列保持最末值即可

"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        while nums and len(nums) > 1 and nums[0] == nums[1]:
            nums = nums[1:]
        n = len(nums)
        if n <= 2:
            return n
        add, pre, res = nums[0] < nums[1], nums[1], 2
        for i in range(2, n):
            if add and nums[i] < pre or not add and nums[i] > pre:
                pre = nums[i]
                add = not add
                res += 1
            pre = nums[i]
        return res
