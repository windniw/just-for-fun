"""

link: https://leetcode.com/problems/fraction-to-recurring-decimal

problem: 分数转小数

solution: 循环节用余数做记录，注意负数情况python的取整有区别，全转正数后加符号

"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        r = "-" if (numerator < 0) ^ (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        n1, n2 = r + str(numerator // denominator), ""
        mods = {}
        t = numerator % denominator
        while t not in mods and t != 0:
            mods[t] = len(n2)
            n2 += str(t * 10 // denominator)
            t = t * 10 % denominator
        if n2 == "":
            return n1
        if t == 0:
            return n1 + "." + n2
        return n1 + "." + n2[:mods[t]] + "(" + n2[mods[t]:] + ")"
