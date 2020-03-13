"""

link: https://leetcode.com/problems/nim-game

problem: 石子游戏，两人轮流拿，每次拿走 1-3 个石子，最后一个拿走的人胜。问先手是否必胜局面。

solution: 0, 4, 8, 12...为必败局，反之可胜

"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0