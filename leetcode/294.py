"""

link: https://leetcode-cn.com/problems/flip-game-ii

problem: 给定一个只含 +- 的字符串，两人轮流将 ++ 变成 --，直至有一方不能操作，判负，问是否有先手必胜策略

solution: SG 函数。显然在这个游戏中，不连续的 +++... 序列间互不影响，求每段长为k的连续+序列的sg值，再异或每段 + 序列的sg值，判其是否处于必败状态。
          对长度为 k 的 + 序列，有 sg(k) = mex{sg(i) ^ sg(k-2-i) | i ∈ [0, k//2]}

"""
def get_sg(n: int) -> [int]:
    f = [0 for _ in range(n + 1)]

    @functools.lru_cache(maxsize=None)
    def sg(k: int):
        if k == 0 or k == 1:
            return 0
        t = set()
        for i in range(k // 2):
            t.add(sg(i) ^ sg(k - 2 - i))
        for i, x in enumerate(sorted(list(t))):
            if i != x:
                return i
        return len(t)

    for i in range(2, n + 1):
        f[i] = sg(i)
    return f


class Solution:
    def canWin(self, s: str) -> bool:
        t, cnt = [], 0
        for x in s:
            if x == '+':
                cnt += 1
            else:
                if cnt != 0:
                    t.append(cnt)
                cnt = 0
        t.append(cnt)
        f, res = get_sg(max(t)), 0
        for k in t:
            res ^= f[k]
        return res != 0
