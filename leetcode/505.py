"""

link: https://leetcode-cn.com/problems/the-maze-ii

problem: 求二维迷宫矩阵中，小球从 A 点到 B 点的最短路径，小球只能沿一个方向滚动直至碰壁

solution: BFS。广搜反复松弛，检查目标点是否优于之前搜索结果。

"""
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1
        n, m, q = len(maze), len(maze[0]), [(start[0], start[1])]
        visit = [[-1 for _ in range(m)] for _ in range(n)]
        visit[start[0]][start[1]] = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q[0][0], q[0][1]
            q.pop(0)
            for ii, jj in d:
                i, j, cnt = x + ii, y + jj, 1
                while 0 <= i < n and 0 <= j < m and maze[i][j] == 0:
                    i, j = i + ii, j + jj
                    cnt += 1
                i, j = i - ii, j - jj
                cnt -= 1
                if visit[i][j] == -1 or visit[i][j] > visit[x][y] + cnt:
                    visit[i][j] = visit[x][y] + cnt
                    q.append((i, j))
        return visit[destination[0]][destination[1]]
