"""

link: https://leetcode-cn.com/problems/shortest-bridge

problem: 给 0 / 1 矩阵，1 代表陆地，0 代表海洋。图中有且仅有两片互相独立的陆地，求两者的最短距离。

solution: DFS + 剪枝搜索。做一轮DFS找到每片陆地的1位置，暴力枚举两者间每个点的距离，其最小值为所求。直接暴会超时，加个简单的剪枝，
          当行距离已经超过当前最优解时直接跳过整行。

solution-fix: DFS + BFS。两两枚举太暴力了，直接以第一片陆地为起点做BFS即可得到最短路。

"""
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        visit = [[-1 for _ in range(m)] for _ in range(n)]
        cur = 0
        island = [[[] for _ in range(n)] for _ in range(2)]

        def dfs(i: int, j: int, color):
            if A[i][j] == 0 or visit[i][j] != -1:
                return
            visit[i][j] = color
            island[color][i].append(j)
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + ii, j + jj
                if 0 <= x < n and 0 <= y < m:
                    dfs(x, y, color)

        for i in range(n):
            for j in range(m):
                if A[i][j] == 1 and visit[i][j] == -1:
                    dfs(i, j, cur)
                    cur += 1

        res = n + m
        for i in range(n):
            for j in island[0][i]:
                for ii in range(n):
                    di = 0 if i == ii else abs(i - ii)
                    if di > res:
                        continue
                    for jj in island[1][ii]:
                        dis = di + abs(j - jj) - 1
                        res = min(res, dis)
        return res

# ---
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        island = []

        def dfs(i: int, j: int):
            if A[i][j] == 0 or A[i][j] == -1:
                return
            A[i][j] = -1
            island.append((i, j))
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + ii, j + jj
                if 0 <= x < n and 0 <= y < m:
                    dfs(x, y)

        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break

        q = [i for i in island]
        while q:
            t = q.pop(0)
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y, c = t[0] + ii, t[1] + jj, A[t[0]][t[1]]
                if 0 <= x < n and 0 <= y < m:
                    if A[x][y] == 1:
                        return -c - 1
                    if A[x][y] == 0:
                        A[x][y] = c - 1
                        q.append((x, y))
