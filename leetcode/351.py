"""

link: https://leetcode-cn.com/problems/android-unlock-patterns

problem: 求所有经过点数为 [m, n] 的合法解锁手势数量

solution: dfs + 记忆化。set 不好做 lru_cache，用位运算替代，构造所有可能并检查，尽早剪枝。

"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        mid = {
            (1, 3): 2,
            (3, 1): 2,
            (1, 7): 4,
            (7, 1): 4,
            (1, 9): 5,
            (9, 1): 5,
            (3, 7): 5,
            (7, 3): 5,
            (3, 9): 6,
            (9, 3): 6,
            (7, 9): 8,
            (9, 7): 8,
            (2, 8): 5,
            (8, 2): 5,
            (4, 6): 5,
            (6, 4): 5,
        }

        @functools.lru_cache(maxsize=None)
        def f(visit: int, cur: int, l: int) -> int:
            if l == 0:
                return 1
            t = 0
            for i in range(1, 10):
                if visit & (1 << i) == 0:
                    if (cur, i) in mid and visit & (1 << mid[(cur, i)]) == 0:
                        continue
                    t += f(visit | (1 << i), i, l - 1)
            return t

        res = 0
        for i in range(m, n + 1):
            for j in range(1, 10):
                res += f(1 << j, j, i - 1)
        return res
