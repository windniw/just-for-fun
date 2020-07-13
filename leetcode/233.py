"""

link: https://leetcode-cn.com/problems/number-of-digit-one

problem: 计算 [0,n] 中数字1的总数

solution: 按位拆分，分别计算个、十、百...位上的1数量

"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        res, k = 0, 1
        while k <= n:
            res += n // (k * 10) * k + max(0, min(n % (k * 10) - k + 1, k))
            k *= 10
        return res
