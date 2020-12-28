"""

link: https://leetcode-cn.com/problems/base-7

problem: 求数字的 7 进制转换

solution: 模7取反，注意符号

"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res, t = "", num
        num = abs(num)
        while num:
            res += str(num % 7)
            num //= 7
        res = res[::-1]
        return res if t >= 0 else "-" + res
