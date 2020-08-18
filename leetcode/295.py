"""

link: https://leetcode-cn.com/problems/find-median-from-data-stream

problem: 实现中位数的在线算法

solution: 二分 + 插入。每次维护数据有序，插入时间O(n), 查询O(1)

solution-fix: 大根堆 + 小根堆。维护小于中位数的大根堆，大于中位数的小根堆，插入后两边不平衡时由少数向多数pop && push。插入时间O(logn)，查询O(1)

"""
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.data)
        while l < r:
            mid = (l + r) >> 1
            if self.data[mid] < num:
                l = mid + 1
            else:
                r = mid
        self.data.insert(l, num)

    def findMedian(self) -> float:
        n = len(self.data)
        if n & 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2

    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()

# ---
class Heap:
    def __init__(self):
        self.data = []
        self.k = 1

    def max_heap(self):
        self.k = -1
        return self

    def top(self):
        return self.data[0] * self.k

    def pop(self):
        return self.k * heapq.heappop(self.data)

    def push(self, item):
        return heapq.heappush(self.data, item * self.k)

    def len(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class MedianFinder:

    def __init__(self):
        self.min_part = Heap().max_heap()
        self.max_part = Heap()

    def addNum(self, num: int) -> None:
        m1, m2 = self.min_part, self.max_part
        m1.push(num) if not m1.empty() and num < m2.top() else m2.push(num)
        while m2.len() > m1.len() + 1:
            m1.push(m2.pop())
        while m1.len() > m2.len() + 1:
            m2.push(m1.pop())

    def findMedian(self) -> float:
        l1, l2 = self.min_part.len(), self.max_part.len()
        if l1 > l2:
            return self.min_part.top()
        elif l1 < l2:
            return self.max_part.top()
        else:
            return (self.min_part.top() + self.max_part.top()) / 2
