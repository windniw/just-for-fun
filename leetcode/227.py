"""

link: https://leetcode.com/problems/basic-calculator-ii

problem: 解析并计算表达式，仅有 +-/* 数字 空格

solution: 模拟栈运算

"""
class Solution:
    def calculate(self, s: str) -> int:
        s = s.rstrip(' ') + "$"
        nl, fl = [], []
        cur = 0
        for x in s:
            if x == ' ':
                continue
            if str.isdigit(x):
                cur = cur * 10 + ord(x) - 48
            else:
                if not fl or fl[-1] == '+' or fl[-1] == '-':
                    nl.append(cur)
                else:
                    f = fl.pop()
                    t = nl.pop()
                    nl.append(t * cur) if f == '*' else nl.append(t // cur)
                cur = 0
                if x != '$':
                    fl.append(x)
        res = nl[0]
        for i in range(len(fl)):
            res = res + nl[i + 1] if fl[i] == '+' else res - nl[i + 1]
        return res
