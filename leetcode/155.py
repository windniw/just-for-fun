"""

link: https://leetcode-cn.com/problems/min-stack

problem: 实现栈

solution: 数组模拟

"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        t = self.data[-1]
        self.data = self.data[0:-1]
        return t

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)
