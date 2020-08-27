"""

link: https://leetcode-cn.com/problems/range-sum-query-2d-mutable

problem: 实现在线的矩阵求和算法

solution: 二维线段树。四分矩形。

"""
class SegmentTree2D:
    def __init__(self, a, b, c, d, x):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.a_son, self.b_son, self.c_son, self.d_son = None, None, None, None
        self.sum = x

    def update(self, x: int, y: int, k: int):
        if self.a == self.c == x and self.b == self.d == y:
            self.sum = k
            return
        mid_x, mid_y = (self.a + self.c) >> 1, (self.b + self.d) >> 1
        if x <= mid_x and y <= mid_y:
            self.a_son.update(x, y, k)
        elif x <= mid_x and y > mid_y:
            self.b_son.update(x, y, k)
        elif x > mid_x and y <= mid_y:
            self.c_son.update(x, y, k)
        else:
            self.d_son.update(x, y, k)
        self.sum = 0
        for son in [self.a_son, self.b_son, self.c_son, self.d_son]:
            self.sum += son.sum if son else 0

    def search(self, a, b, c, d) -> int:
        if self.a == a and self.b == b and self.c == c and self.d == d:
            return self.sum
        mid_x, mid_y = (self.a + self.c) >> 1, (self.b + self.d) >> 1
        res = 0
        if a <= mid_x and b <= mid_y:
            res += self.a_son.search(a, b, min(c, mid_x), min(d, mid_y))
        if a <= mid_x and d > mid_y:
            res += self.b_son.search(a, max(b, mid_y + 1), min(c, mid_x), d)
        if c > mid_x and b <= mid_y:
            res += self.c_son.search(max(a, mid_x + 1), b, c, min(d, mid_y))
        if c > mid_x and d > mid_y:
            res += self.d_son.search(max(a, mid_x + 1), max(b, mid_y + 1), c, d)
        return res


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        def build(a, b, c, d) -> SegmentTree2D:
            if a > c or b > d:
                return None
            x = SegmentTree2D(a, b, c, d, 0)
            if a == c and b == d:
                x.sum = matrix[a][b]
                return x
            mid_x, mid_y = (a + c) >> 1, (b + d) >> 1
            x.a_son = build(a, b, mid_x, mid_y)
            x.b_son = build(a, mid_y + 1, mid_x, d)
            x.c_son = build(mid_x + 1, b, c, mid_y)
            x.d_son = build(mid_x + 1, mid_y + 1, c, d)
            for son in [x.a_son, x.b_son, x.c_son, x.d_son]:
                x.sum += son.sum if son else 0
            return x

        if len(matrix) and len(matrix[0]):
            self.t = build(0, 0, len(matrix) - 1, len(matrix[0]) - 1)

    def update(self, row: int, col: int, val: int) -> None:
        if self.t:
            self.t.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.t.search(row1, col1, row2, col2) if self.t else 0
