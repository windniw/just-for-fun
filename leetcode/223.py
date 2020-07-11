"""

link: https://leetcode-cn.com/problems/rectangle-area

problem: 给坐标系内的两个矩形，求其重叠后的总面积

solution: 重叠面积 = 两矩形面积 - 相交形成矩形的面积

"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        h = min(D, H) - max(B, F)
        w = min(C, G) - max(A, E)
        d = 0 if h < 0 or w < 0 else h * w
        return (C - A) * (D - B) + (G - E) * (H - F) - d
