"""

link: https://leetcode.com/problems/majority-element

problem: 求数组中的多数值

solution: map记录

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = collections.defaultdict(int)
        for x in nums:
            m[x] += 1
        for x in m:
            if m[x] > len(nums) / 2:
                return x
