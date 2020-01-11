"""

link: https://leetcode.com/problems/number-of-1-bits

problem: 统计1个数

solution: 位移

"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
