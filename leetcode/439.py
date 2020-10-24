"""

link: https://leetcode-cn.com/problems/ternary-expression-parser

problem: 解析三元表达式，格式一定合法。

solution: 递归解析。

"""
class Solution:
    def parseTernary(self, expression: str) -> str:
        i, n = 0, len(expression)

        def get_expr() -> str:
            nonlocal i
            if i == n - 1 or expression[i + 1] == ':':
                t = expression[i]
                i += 2
                return t
            key = expression[i]
            i += 2
            a = get_expr()
            b = get_expr()
            return a if key == 'T' else b

        return get_expr()
