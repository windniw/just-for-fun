"""

link: https://leetcode.com/problems/missing-number

problem: 从 [0,n] 的乱序序列中取走一个数，求取走的数，要求时间O(n)，空间O(1)

solution: 求原序列和，减当前序列和

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)
