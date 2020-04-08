"""

link: https://leetcode.com/problems/intersection-of-two-arrays

problem: 求数组交集

solution: 转集合求交

"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        return list(a.intersection(b))
