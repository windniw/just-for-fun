"""

link: https://leetcode-cn.com/problems/the-maze

problem: 给 0，1 矩阵代表迷宫，0 为空地，1为墙，规定移动必须沿一个方向直至碰到墙或边界，问能否从起始点到达终点

solution: dfs

"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])

        def dfs(i: int, j: int) -> bool:
            if i == destination[0] and j == destination[1]:
                return True
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i, j
                while 0 <= x + ii < n and 0 <= y + jj < m and maze[x + ii][y + jj] != 1:
                    x += ii
                    y += jj
                if maze[x][y] != 2:
                    maze[x][y] = 2
                    if dfs(x, y):
                        return True

            return False

        maze[start[0]][start[1]] = 2
        return dfs(start[0], start[1])
