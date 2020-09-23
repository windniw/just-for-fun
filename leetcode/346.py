"""

link: https://leetcode-cn.com/problems/moving-average-from-data-stream

problem: 维护定长流数组均值

solution: 记录流，更好的做法是用环形数组。

"""
class MovingAverage:

    def __init__(self, size: int):
        self.data = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.data) == self.size:
            self.data = self.data[1:]
        self.data.append(val)
        return sum(self.data) / len(self.data)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)