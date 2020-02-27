"""

link: https://leetcode.com/problems/add-digits

problem: 将给定数字各位相加，重复直至数字小于10

solution: 递归

"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 == 0:
            return num
        n = 0
        while num:
            n += num % 10
            num //= 10
        return self.addDigits(n)
