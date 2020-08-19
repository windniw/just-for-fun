"""

link: https://leetcode-cn.com/problems/best-meeting-point

problem: 给0,1组成的二维矩阵，求矩阵中与所有的1总曼哈顿距离最小的点

solution: 显然，x, y轴是相互独立的。先找出所有 1 的位置，将其横纵坐标各存入一个数组，问题转换成在两个一维数组中，分别找到与其他点距离最小的
          整数值并相加。在数组长度为2时，任何在中间的点距离均相等，在数组有多个元素时，该值为数组的中位数。
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        p1, p2, n, m = [], [], len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    p1.append(i)
                    p2.append(j)

        def avg(k: [int]) -> int:
            k.sort()
            t, n = 0, len(k)
            for i in range(n // 2):
                t += k[n - 1 - i] - k[i]
            return t

        return avg(p1) + avg(p2)
