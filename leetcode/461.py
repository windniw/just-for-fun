"""

link: https://leetcode-cn.com/problems/hamming-distance

problem: 求两个数字的二进制表达式中不同的位数量

solution: 消除异或结果最右的1

"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, cnt = x ^ y, 0
        while x:
            x &= (x - 1)
            cnt += 1
        return cnt
