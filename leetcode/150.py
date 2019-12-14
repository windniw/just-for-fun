"""

link: https://leetcode.com/problems/evaluate-reverse-polish-notation

problem: 求逆序表达式

solution: 栈模拟即可。最大的问题在于python的标准和C不一样... 1 // -2 等于 -1 而不是 0，
因为C标准是向0取整，python标准是向无穷取整，题目要求前者，用int(a/b)代替 a//b

"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = {
            "+": lambda b, a: a + b,
            "-": lambda b, a: a - b,
            "*": lambda b, a: a * b,
            "/": lambda b, a: int(a / b)
        }
        for x in tokens:
            if x in op:
                s.append(op[x](s.pop(), s.pop()))
            else:
                s.append(int(x))
        return s[0]
