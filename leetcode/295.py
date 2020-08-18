"""

link: https://leetcode-cn.com/problems/find-median-from-data-stream

problem: 实现中位数的在线算法

solution: 二分 + 插入。每次维护数据有序，插入时间O(n), 查询O(1)

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
