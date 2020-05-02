"""

link: https://leetcode.com/problems/sum-of-two-integers 

problem: 不用 + / - 号，求 integer 类型的 a + b

solution: 由于python没有左移整形溢出这道题难度直线上升。 
          a + b 
          == 不进位 (a + b) + 进位 (a + b) << 1
          == a ^ b + (a & b) << 1
          持续迭代到 (a & b) << 1 为0，即不进位时, 结果为当时的 a ^ b

"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_uint = 0xffffffff
        max_int = 0x7fffffff - 1
        while a:
            add = (a & b) << 1
            b = a ^ b
            a = add
            add &= max_uint
            b &= max_uint
        return b if b <= max_int else ~(b ^ max_uint)
