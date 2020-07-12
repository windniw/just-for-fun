"""

link: https://leetcode-cn.com/problems/basic-calculator

problem: 求解表达式，包含 + - ( ) 四种操作符

solution: 按序扫一遍，'(' 入栈作为分隔符。

solution-fix: 本题只有 + - 没有乘除，将 a - b 表达成 a + (-b)，123 表达成 120 + 2 + 3。每次碰到'('括号，暂存括号前的计算结果，
              将括号视为新的运算过程开始，并在')'括号时与之前结果进行合并。

"""
class Solution:
    def calculate(self, s: str) -> int:
        i, n, res_stack = 0, len(s), []

        def read_next():
            nonlocal i
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                return None
            if s[i] in '()+-':
                i += 1
                return s[i - 1]
            t = 0
            while i < n and '0' <= s[i] <= '9':
                t = t * 10 + ord(s[i]) - 48
                i += 1
            return t

        t = read_next()
        while t is not None:
            if t == ')':
                k = res_stack[-1]
                res_stack.pop()
                res_stack.pop()
                t = k
                continue
            elif t == '(' or t == '+' or t == '-':
                res_stack.append(t)
            else:
                if not res_stack or res_stack[-1] == '(':
                    res_stack.append(t)
                else:
                    op = res_stack[-1]
                    k = res_stack[-2]
                    res_stack.pop()
                    res_stack.pop()
                    res_stack.append(k - t if op == '-' else k + t)
            t = read_next()
        return res_stack[0]

# ---
class Solution:
    def calculate(self, s: str) -> int:
        sign, num, res, res_stack = 1, 0, 0, []
        for c in s:
            if '0' <= c <= '9':
                num = num * 10 + ord(c) - 48
            if c == '+' or c == '-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            if c == '(':
                res_stack.append(res)
                res_stack.append(sign)
                res = 0
                sign = 1
            if c == ')':
                res += sign * num
                res *= res_stack.pop()
                res += res_stack.pop()
                num = 0
        return res + sign * num
