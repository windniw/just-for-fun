"""

link: https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix

problem: 求给定矩阵的最大严格递增路径长度

solution: DP。从小到大排序所有元素，因为路径只能从低向高长，g[i][j] 记录当检查到 matrix[i][j] 时，以 matrix[i][j] 为终点的最大路径长度。
          因为做了排序，时间复杂度O(nm(log_nm))

solution-fix: 拓扑排序。思路同上，不做排序，遍历一次记录每个点附近比其小的点数量作为入度，用拓扑序遍历，时间复杂度可以压到 O(nm)

"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m, q = len(matrix), len(matrix[0]), []
        g = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                q.append((matrix[i][j], i, j))
        q.sort()
        res = 1
        for k in q:
            x, y, t = k[1], k[2], 1
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = x + ii, y + jj
                if 0 <= i < n and 0 <= j < m and matrix[i][j] < matrix[x][y] and g[i][j] + 1 > t:
                    t = g[i][j] + 1
            g[x][y] = t
            res = max(res, t)
        return res

# ---
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m, q = len(matrix), len(matrix[0]), []
        g = [[[1, 0] for _ in range(m)] for _ in range(n)]
        for x in range(n):
            for y in range(m):
                for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i, j = x + ii, y + jj
                    if 0 <= i < n and 0 <= j < m and matrix[i][j] < matrix[x][y]:
                        g[x][y][1] += 1
                if g[x][y][1] == 0:
                    q.append((x, y))
        res = 1
        while q:
            k = q.pop()
            x, y = k[0], k[1]
            res = max(res, g[x][y][0])
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i, j = x + ii, y + jj
                if 0 <= i < n and 0 <= j < m and matrix[i][j] > matrix[x][y]:
                    g[i][j][0] = max(g[i][j][0], g[x][y][0] + 1)
                    g[i][j][1] -= 1
                    if g[i][j][1] == 0:
                        q.append((i, j))
        return res
