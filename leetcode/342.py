"""

link: https://leetcode.com/problems/power-of-four

problem: 问num是否是4的幂，要求O(1)

solution: 位运算

"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
