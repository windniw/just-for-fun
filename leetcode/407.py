
"""

link: https://leetcode-cn.com/problems/trapping-rain-water-ii

problem: 给二维矩阵代表每个点的高度，向其最大的保留水量，设周围高度为0

solution: 维护边沿，用最小堆每次抛出边缘的最小值，依次向内收缩做搜索。

"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        heap, n, m = [], len(heightMap), len(heightMap[0])
        visit = [[False] * m for _ in range(n)]
        visit[0][0] = visit[0][-1] = visit[-1][0] = visit[-1][-1] = True
        for i in range(1, n - 1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][-1], i, m - 1))
            visit[i][0] = visit[i][-1] = True
        for i in range(1, m - 1):
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            heapq.heappush(heap, (heightMap[-1][i], n - 1, i))
            visit[0][i] = visit[-1][i] = True
        res = 0
        while heap:
            (v, i, j) = heapq.heappop(heap)
            for ii, jj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                x, y = i + ii, j + jj
                if 0 <= x < n and 0 <= y < m and not visit[x][y]:
                    visit[x][y] = True
                    if heightMap[x][y] >= v:
                        heapq.heappush(heap, (heightMap[x][y], x, y))
                    else:
                        heapq.heappush(heap, (v, x, y))
                        res += v - heightMap[x][y]
        return res
