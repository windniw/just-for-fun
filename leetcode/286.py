"""

link: https://leetcode-cn.com/problems/walls-and-gates

problem: 用矩阵代表空间，0为门，-1为墙, 2**31-1为空房间，求每个空房间到门的最短距离。

solution: BFS。滑雪问题，从每个门开始做bfs，更新距离时入队直至没有房间被更新。

"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        q, n, m = [], len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.pop()
            cur = rooms[i][j]
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + ii < n and 0 <= j + jj < m and rooms[i + ii][j + jj] > cur + 1:
                    rooms[i + ii][j + jj] = cur + 1
                    q.append((i + ii, j + jj))
        return
