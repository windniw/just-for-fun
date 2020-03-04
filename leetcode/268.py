"""

link: https://leetcode.com/problems/missing-number

problem: 从 [0,n] 的乱序序列中取走一个数，求取走的数，要求时间O(n)，空间O(1)

solution: 求原序列和，减当前序列和

solution-fix: 求和可能有溢出风险，用异或也可。求原序列异或和，异或当前序列异或和，即为缺失数

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)

# ---
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, x = len(nums), 0
        for i in range(n + 1):
            x ^= i
        for i in nums:
            x ^= i
        return x