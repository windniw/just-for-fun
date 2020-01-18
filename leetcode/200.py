"""

link: https://leetcode.com/problems/number-of-islands

problem: 输出矩阵中有多少块连续的1

solution: DFS

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return
        n, m, res = len(grid), len(grid[0]), 0

        def color(i: int, j: int):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if grid[i][j] != '1':
                return False
            grid[i][j] = '2'
            color(i - 1, j)
            color(i + 1, j)
            color(i, j - 1)
            color(i, j + 1)
            return True

        for i in range(n):
            for j in range(m):
                if color(i, j):
                    res += 1

        return res