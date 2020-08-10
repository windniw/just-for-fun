"""

link: https://leetcode-cn.com/problems/zigzag-iterator

problem: 实现迭代器，能够循环返回初始化k个数组中的元素

solution: 预初始化，整合丢尽新的list数组

"""
class ZigzagIterator:
    class Item:
        def __init__(self, v: List[int]):
            self.i = 0
            self.list = v

    def __init__(self, v1: List[int], v2: List[int]):
        t = [self.Item(v1), self.Item(v2)]
        num, data, cnt, ci = len(v1) + len(v2), [], 0, 0
        while cnt < num:
            if t[ci].i < len(t[ci].list):
                data.append(t[ci].list[t[ci].i])
                cnt += 1
                t[ci].i += 1
            ci += 1
            if ci >= len(t):
                ci = 0
        self.data = data
        self.i = 0

    def next(self) -> int:
        self.i += 1
        return self.data[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.data)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())