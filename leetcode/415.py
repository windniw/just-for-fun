"""

link: https://leetcode.com/problems/add-strings

problem: 实现字符串加法

solution: 按位倒序加

"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2, num1 = num1, num2
        num1 = (len(num2) - len(num1)) * "0" + num1
        add, res = 0, ""
        for i in reversed(range(len(num1))):
            t = ord(num1[i]) + ord(num2[i]) - 96 + add
            res = chr(t % 10 + 48) + res
            add = t // 10
        return res if not add else "1" + res
