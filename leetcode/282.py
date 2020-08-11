"""

link: https://leetcode-cn.com/problems/expression-add-operators

problem: 给纯数字字符串，对其补充 +-* 三种运算符，求补完算式结果为 target 的所有可能

solution: 暴力枚举后求表达式结果。

"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def cal(k: str) -> int:
            k += '+'
            c, stack, minus, pre_op = 0, [], 1, '+'
            for x in k:
                if x in '0123456789':
                    c = c * 10 + ord(x) - 48
                elif x in '*+-':
                    if pre_op == '*':
                        stack[-1] = stack[-1] * c * minus
                    else:
                        stack.append(c * minus)
                    pre_op = x
                    c = 0
                    minus = -1 if x == '-' else 1
            return sum(stack)

        res = []

        def dfs(k: str, i: int):
            if i + 1 >= len(k):
                if cal(k) == target:
                    res.append(k)
                return
            for x in "*+-":
                dfs(k[:i + 1] + x + k[i + 1:], i + 2)
            if k[i] == '0' and (i == 0 or k[i - 1] in "+-*"):
                return
            dfs(k, i + 1)

        dfs(num, 0)
        return res
