"""

link: https://leetcode-cn.com/problems/design-hit-counter

problem: 多次输入，每次一个时间戳，代表该时间点触发一次；多次询问，求询问时间的前300秒内，共触发几次，考虑极度密集场景，样例按时间顺序输入

solution: 滚动数组。稀疏时可以直接双端队列记录每个触发点的时间；极度密集时队列太大，而时间点是常量
          维护一个长度为 300 的滚动数组，每个位置代表该时间点的触发次数，循环滚动。

"""
class HitCounter:

    def __init__(self):
        self.n = 10
        self.data = [0] * self.n
        self.head = 0
        self.headp = 0

    def p(self, id) -> int:
        return (self.headp + id - self.head) % self.n

    def roll(self, new_head):
        if new_head <= self.head:
            return
        if new_head > self.head + self.n:
            for i in range(self.n):
                self.data[i] = 0
            self.headp = self.p(new_head)
            self.head = new_head
            return
        for i in range(self.head, new_head):
            self.data[self.p(i)] = 0
        self.headp = self.p(new_head)
        self.head = new_head

    def hit(self, timestamp: int) -> None:
        self.roll(timestamp - self.n + 1)
        self.data[self.p(timestamp)] += 1

    def getHits(self, timestamp: int) -> int:
        self.roll(timestamp - self.n + 1)
        return sum(self.data)
