"""

link: https://leetcode-cn.com/problems/island-perimeter

problem: 求二维矩阵中，1组成的图形的周长，1只会组成一块图形，不会分割，没有中空的情况

solution: 扫一遍检查1与0的边数量

"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m, res = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + ii, j + jj
                    if (not (0 <= x < n and 0 <= y < m)) or grid[x][y] == 0:
                        res += 1
        return res
