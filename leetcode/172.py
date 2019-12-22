"""

link: https://leetcode.com/problems/factorial-trailing-zeroes

problem: 求 n! 末尾0的数量

solution: 阶乘中每个数5的因数数量

"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x, res = 5, 0
        while x <= n:
            res += n // x
            x *= 5
        return res
