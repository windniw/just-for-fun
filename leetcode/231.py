"""

link: https://leetcode.com/problems/power-of-two

problem: 判断数字是否是2的幂

solution: 去除首位1后判断是否为0

"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0