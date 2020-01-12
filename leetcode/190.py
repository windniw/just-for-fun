"""

link: https://leetcode.com/problems/reverse-bits

problem: 翻转32位无符号整数

solution: 循环左移

"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res
