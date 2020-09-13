"""

link: https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix

problem: 求给定矩阵的最大严格递增路径长度

solution: DP。从小到大排序所有元素，因为路径只能从低向高长，g[i][j] 记录当检查到 matrix[i][j] 时，以 matrix[i][j] 为终点的最大路径长度。
          因为做了排序，时间复杂度O(nm(log_nm))

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
