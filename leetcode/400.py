"""

link: https://leetcode.com/problems/nth-digit

problem: 求 1, 2...  无限序列中的第n个数字

solution: 1位数字的有9个，2位90个，3位900个；先找n对应的数字是多少，然后返回其位数

"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        num = 1
        while n > num * 9 * 10 ** (num - 1):
            n -= num * 9 * 10 ** (num - 1)
            num += 1
        a, b = n // num, n % num
        a += 1 if b else 0
        b = b if b else num
        a += 10 ** (num - 1) - 1
        return int(str(a)[b-1:b])