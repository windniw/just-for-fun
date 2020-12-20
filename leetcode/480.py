"""

link: https://leetcode-cn.com/problems/sliding-window-median

problem: 给数组和与滑动窗口长度 k，求数组从左向右每个窗口的中位数

solution: 大顶堆 + 小顶堆。思路类似 295，由于多了一个删除操作，增加一个 multiset 做延迟删除。

"""
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


class MultiSet:
    def __init__(self):
        self.data = {}

    def add(self, x):
        if x not in self.data:
            self.data[x] = 0
        self.data[x] += 1

    def remove(self, x):
        self.data[x] -= 1
        if self.data[x] == 0:
            del (self.data[x])

    def contains(self, x) -> bool:
        return x in self.data


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res, m1, m2, cache, balance = [], Heap().max_heap(), Heap(), MultiSet(), 0
        for i, x in enumerate(nums):
            if m1.empty() or x <= m1.top():
                m1.push(x)
                balance += 1
            else:
                m2.push(x)
                balance -= 1
            if i >= k:
                cache.add(nums[i - k])
                balance += -1 if nums[i - k] <= m1.top() else 1
            while balance != 0 and balance != 1 or not m1.empty() and cache.contains(
                    m1.top()) or not m2.empty() and cache.contains(
                    m2.top()):
                if balance > 1:
                    m2.push(m1.pop())
                    balance -= 2
                if balance < 0:
                    m1.push(m2.pop())
                    balance += 2
                while not m1.empty() and cache.contains(m1.top()):
                    cache.remove(m1.pop())
                while not m2.empty() and cache.contains(m2.top()):
                    cache.remove(m2.pop())
            if i >= k - 1:
                if balance == 0:
                    res.append((m1.top() + m2.top()) / 2)
                else:
                    res.append(m1.top() if balance == 1 else m2.top())
        return res