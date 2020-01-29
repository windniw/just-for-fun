"""

link: https://leetcode.com/problems/implement-stack-using-queues

problem: 用队列实现栈

solution: 每次入栈的时候翻转两次队列

"""
class MyStack:

    def __init__(self):
        self.data = collections.deque()

    def push(self, x: int) -> None:
        self.data.reverse()
        self.data.appendleft(x)
        self.data.reverse()

    def pop(self) -> int:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0
