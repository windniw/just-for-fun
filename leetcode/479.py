"""

link: https://leetcode-cn.com/problems/largest-palindrome-product

problem: 求两个 N 位数相乘的最大回文数

solution: 打表。从大向下枚举 2*N 的所有回文数，检查其能否由两个 N 位整数相乘组成。

"""
class Solution:
    def largestPalindrome(self, n: int) -> int:
        def check(k: int):
            for i in range(10 ** (n - 1), 10 ** n):
                if k // i >= 10 ** n:
                    continue
                if k % i == 0:
                    exit(0)
            return

        def g(i: int, t: int):
            if i >= n:
                x = str(t)
                check(int(x + x[::-1]))
                return
            for j in reversed(range(10)):
                if i == 0 and j == 0:
                    continue
                g(i + 1, t * 10 + j)

        def gg(i: int, t: int):
            if i >= n:
                x = str(t)
                check(int(x + x[:-1][::-1]))
                return
            for j in reversed(range(10)):
                if i == 0 and j == 0:
                    continue
                gg(i + 1, t * 10 + j)

        # g(0, 0)
        # gg(0, 0)

        res = [0, 9 % 1337,
               9009 % 1337,
               906609 % 1337,
               99000099 % 1337,
               9966006699 % 1337,
               999000000999 % 1337,
               99956644665999 % 1337,
               9999000000009999 % 1337]
        return res[n]