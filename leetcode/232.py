"""

link: https://leetcode.com/problems/implement-queue-using-stacks

problem: 用栈实现队列

solution: push时用另一个栈临时转移数据，维持栈中的数据为队列的顺序

"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        t = []
        while self.data:
            t.append(self.data.pop())
        self.data.append(x)
        while t:
            self.data.append(t.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.data.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) == 0
