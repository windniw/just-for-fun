"""

link: https://leetcode-cn.com/problems/line-reflection

problem: 给坐标轴内 n 个点，问能否找到一条垂直于 x 轴的直线使给定点对称，要求时间小于 O(n^2)，注意给定的点可能重复

solution: 去重，排序，检查。时间 O(nlogn)

"""
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = list(set([(a, b) for a, b in points]))
        n, r_points = len(points), points.copy()
        points.sort()
        r_points.sort(key=lambda x: (-x[0], x[1]))
        mid = (points[0][0] + r_points[0][0]) / 2
        for i in range((n + 1) // 2):
            if not ((points[i][0] + r_points[i][0]) / 2 == mid and (points[i][1] == r_points[i][1])):
                return False
        return True
