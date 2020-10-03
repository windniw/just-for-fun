"""

link: https://leetcode-cn.com/problems/bomb-enemy

problem: 模拟炸弹游戏，用 'E' 代表敌人，'0' 代表空地，'W' 代表墙，在任何空地放炸弹可以炸到同行同列的所有敌人但不能穿墙，求放一个炸弹时最大炸到的敌人数 

solution: 向左，向右，向上，向下，依次扫一遍，累计每个空地四个方向的敌人数，时间复杂度O(nm)

"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        res = [[0] * m for _ in range(n)]

        def f(i, j, cnt):
            if grid[i][j] == '0':
                res[i][j] += cnt
            elif grid[i][j] == 'E':
                cnt += 1
            else:
                cnt = 0
            return cnt

        for i in range(n):
            cnt = 0
            for j in range(m):
                cnt = f(i, j, cnt)
        for i in range(n):
            cnt = 0
            for j in reversed(range(m)):
                cnt = f(i, j, cnt)
        for j in range(m):
            cnt = 0
            for i in reversed(range(n)):
                cnt = f(i, j, cnt)
        for j in range(m):
            cnt = 0
            for i in range(n):
                cnt = f(i, j, cnt)
        return max(max(t) for t in res)
