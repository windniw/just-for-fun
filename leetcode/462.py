"""

link: https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii

problem: 定义一次操作为对数组任意元素 +1 或 -1，问至少多少次元素后数组所有元素相等

solution: 相等元素为数组中位数

"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n, res = len(nums), 0
        k = nums[n // 2] if n & 1 else (nums[n // 2] + nums[n // 2 - 1]) // 2
        for v in nums:
            res += abs(v-k)
        return res
