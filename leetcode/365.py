"""

link: https://leetcode.com/problems/count-numbers-with-unique-digits

problem: 求 10**n 之内，每位数字不同的数字的位数

solution: 因为数字只有10个，显然 n 大于10没有意义。转换下问题变成求对每个长度k的数字求A(k,n)并去掉0开头的部分(即 1/10)

"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def f(k: int):
            t = 1
            while k:
                t *= (11 - k)
                k -= 1
            t = t // 10 * 9
            return t

        res = 1
        for i in range(1, n + 1):
            res += f(i)
        return res
