"""

link: https://leetcode-cn.com/problems/number-complement

problem: 对 32 位正整数取反

solution: 用对应全1的二进制减nums

"""
class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(32, -1, -1):
            if (1 << i) & num:
                break
        return (1 << (i + 1)) - 1 - num
