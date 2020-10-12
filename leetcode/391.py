"""

link: https://leetcode-cn.com/problems/perfect-rectangle

problem: 给 N 个用左上，右下坐标标志的矩形，问其能否精确覆盖一个完整的矩形，即不可重叠，覆盖面刚好为一个矩形

solution: 观察，若满足题意的充要条件为，所有矩形之和等于最终矩形面积，且除四个顶点外，每个顶点均出现偶数次

"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s = 0
        f = []
        for x in rectangles:
            s += (x[2] - x[0]) * (x[3] - x[1])
            f.extend([(x[0], x[1]), (x[2], x[3]), (x[0], x[3]), (x[2], x[1])])
        f.sort()

        i, r = 0, []
        while i < len(f):
            if i + 1 < len(f) and f[i] == f[i + 1]:
                i += 2
                continue
            r.append(f[i])
            i += 1
        return len(r) == 4 and (r[3][0] - r[0][0]) * (r[3][1] - r[0][1]) == s
