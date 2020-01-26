"""

link: https://leetcode.com/problems/contains-duplicate

problem: 数组是否存在重复元素

solution: 转集合判长度

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))