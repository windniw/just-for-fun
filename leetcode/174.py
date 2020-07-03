"""

link: https://leetcode-cn.com/problems/dungeon-game

problem: 二维矩阵图，骑士从 (0, 0) 开始走到 (i-1, j-1)，只能向下或向右，每格数字代表加血或减血，要求途中血量不可低于1，求骑士初始的最低血量

solution: DFS。对每个格子，求到达该格时最低血量，每格满足右或下的最小要求即可。

"""
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if len(dungeon) == 0 or len(dungeon[0]) == 0:
            return 1
        n, m = len(dungeon), len(dungeon[0])

        @functools.lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if i >= n or j >= m:
                return float("inf")
            k = dungeon[i][j]
            if i == n - 1 and j == m - 1:
                return 1 if k >= 0 else -k + 1
            t = min(dfs(i, j + 1), dfs(i + 1, j))
            return 1 if k + 1 >= t else t - k

        return dfs(0, 0)
