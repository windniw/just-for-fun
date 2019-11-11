"""

link: https://leetcode.com/problems/interleaving-string

problem: 问s3是否能用s1,s2交错组成。

solution: DP。定义 f[i][j] 为 s1[:i], s2[:j] 能否交错组成 s3[:i+j], 注意i, j=0时，代表空串。有转移式:
          f[i][j] = f[i - 1][j] and s1[i - 1] == s3[i + j - 1] or \
            f[i][j - 1] and s2[j - 1] == s3[i + j - 1]

"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3) or collections.Counter(s1) + collections.Counter(s2) != collections.Counter(s3):
            return False
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True
        for i in range(1, m + 1):
            f[0][i] = f[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, n + 1):
            f[i][0] = f[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j] and s1[i - 1] == s3[i + j - 1] or f[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return f[n][m]