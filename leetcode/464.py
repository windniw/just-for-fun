"""

link: https://leetcode-cn.com/problems/can-i-win

problem: A,B 轮流从 [1, n] 中挑数字加入 s，先使 s 大于或等于 t 的玩家获胜，问先手是否必胜，n <= 20, t <= 300

solution: 状压DP。用 1<<20 来记录数字是否已经被挑选，记必胜点为 win, 必败点为 lost。win 的充要条件为存在任意可达状态为 lost；
          lost 的可达状态为任何可达状态均为 win。

"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @functools.lru_cache(maxsize=None)
        def f(k: int, cur: int):
            if cur >= desiredTotal:
                return False
            for i in range(maxChoosableInteger):
                if (1 << i) & k == 0:
                    if not f(k | (1 << i), cur + i + 1):
                        return True
            return False

        if desiredTotal == 0:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return f(0, 0)
