"""

link: https://leetcode-cn.com/problems/range-sum-query-mutable

problem: 实现在线的区间求和算法

solution: 线段树。

"""
class SegmentTree:
    def __init__(self, l: int, r: int, x: int):
        self.l = l
        self.r = r
        self.sum = x
        self.left_son = None
        self.right_son = None

    def update(self, x: int, i: int):
        if self.l == self.r == i:
            self.sum = x
            return
        mid = (self.l + self.r) >> 1
        if self.l <= i <= mid:
            self.left_son.update(x, i)
        elif mid + 1 <= i <= self.r:
            self.right_son.update(x, i)
        self.sum = self.left_son.sum + self.right_son.sum

    def search(self, l: int, r: int) -> int:
        if self.l == l and self.r == r:
            return self.sum
        mid = (self.l + self.r) >> 1
        if r <= mid:
            return self.left_son.search(l, r)
        elif l >= mid + 1:
            return self.right_son.search(l, r)
        else:
            return self.left_son.search(l, mid) + self.right_son.search(mid + 1, r)


def build(l: int, r: int, v: [int]) -> SegmentTree:
    if len(v) == 0:
        return None
    x = SegmentTree(l, r, v[l])
    if l == r:
        return x
    mid = (l + r) >> 1
    x.left_son = build(l, mid, v)
    x.right_son = build(mid + 1, r, v)
    x.sum = x.left_son.sum + x.right_son.sum
    return x


class NumArray:

    def __init__(self, nums: List[int]):
        self.t = build(0, len(nums) - 1, nums)

    def update(self, i: int, val: int) -> None:
        if self.t:
            self.t.update(val, i)

    def sumRange(self, i: int, j: int) -> int:
        if self.t:
            return self.t.search(i, j)
        else:
            return 0