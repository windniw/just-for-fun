"""

link: https://leetcode.com/problems/ugly-number

problem: 问给的数字是否只有 2，3，5 的因数

solution: 循环除直至1。

"""
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        l = [2, 3, 5]
        for x in l:
            while num % x == 0:
                num //= x
        return num == 1
