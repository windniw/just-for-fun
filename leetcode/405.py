"""

link: https://leetcode.com/problems/convert-a-number-to-hexadecimal

problem: 十进制转16进制，[-2^31, 2^31-1]，不用库函数

solution: 负数转相应unsigned int后，反复取模

"""
class Solution:
    def toHex(self, num: int) -> str:
        def f(x: int) -> str:
            return str(x) if x < 10 else chr(x - 10 + 97)

        if num < 0:
            num = 0x100000000 + num
        res = ""
        while num:
            res += f(num % 16)
            num //= 16
        return res[::-1] if res else '0'