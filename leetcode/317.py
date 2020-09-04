"""

link: https://leetcode-cn.com/problems/shortest-distance-from-all-buildings

problem: 定义数字矩阵的 0 为空地，1 为建筑，2为墙，建筑与墙均不可通行，求找到某一空地与所有建筑相通且距离最短，返回其距离和

solution: BFS。直观的暴力法是枚举空地求到每个建筑的距离，这种搞法会超时。想象一个极度稀疏到没有建筑和墙的图，时间复杂度就会退化成O(n*m*n*m)。但
          反过来，枚举建筑，统计其到每个空地的距离，再扫一遍求这个和的最小值。这种搞法就可以过，因为极度稀疏时，没有可枚举的建筑；极度稠密时，建筑
          不可通行导致入队的空地数极度减少。虽然时间复杂依然为 O(n*m*n*m)，但常数时间优化非常大。

"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        n, m, buildings = len(grid), len(grid[0]), 0
        dis = [[[0, 0] for _ in range(m)] for _ in range(n)]

        def bfs(i, j):
            q, visit = [(i, j, 0)], {(i, j)}
            while q:
                x, y, move = q[0][0], q[0][1], q[0][2]
                q.pop(0)
                for ii, jj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    xx, yy = x + ii, y + jj
                    if 0 <= xx < n and 0 <= yy < m and ((xx, yy) not in visit):
                        visit.add((xx, yy))
                        if grid[xx][yy] == 0:
                            dis[xx][yy][0] += move + 1
                            dis[xx][yy][1] += 1
                            q.append((xx, yy, move + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings +=1
                    bfs(i, j)

        res = float("inf")
        for i in range(n):
            for j in range(m):
                if dis[i][j][1] == buildings:
                    res = min(dis[i][j][0], res)
        return -1 if res == float("inf") else res