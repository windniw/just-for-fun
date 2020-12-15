"""

link: https://leetcode-cn.com/problems/count-the-repetitions

problem: 问 s1*n1 的子序列中包含多少个 s2*n2

solution: 循环节。双指针扫记录每次的位置，找到 i, j 重复出现的循环节加速跳转。

"""
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        if set(s2) - set(s1):
            return 0

        n, m = len(s1), len(s2)
        t = s1 + s1
        f = [{} for _ in range(n)]
        for i in range(n * 2):
            for j in range(min(i - 1, n - 1), -1, -1):
                if t[i] in f[j]:
                    break
                f[j][t[i]] = i % n
        i, j, k1, k2, fk = -1, 0, 0, 0, collections.defaultdict(tuple)

        def get_next():
            nonlocal i, j, k1, k2
            tj = j
            i = f[i][s2[j]] if i != -1 else s1.index(s2[0])
            j = (j + 1) % m
            k1 += f[i][s2[j]] <= i
            k2 += tj >= j

        while k1<n1:
            if (i, j) in fk:
                (kk1, kk2) = fk[(i, j)]
                k2 += (n1 - k1 - 1) // (k1 - kk1) * (k2 - kk2)
                k1 += (n1 - k1 - 1) // (k1 - kk1) * (k1 - kk1)
                while k1 < n1:
                    get_next()
                break
            fk[(i, j)] = k1, k2
            get_next()
        return k2 // n2
