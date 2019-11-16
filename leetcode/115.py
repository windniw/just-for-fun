"""

link: https://leetcode.com/problems/distinct-subsequences

problem: 问s的子序列中有多少个等于t

solution: DP。状态找对了转移方程写飞了。。。定义 f[i][j] 为 (s[:i], t[:j]) 的解，有以下转移式
无论如何有:
    f[i][j] += f[i-1][j]          忽略s[i-1]，直接继承前值
当 s[i-1] == t[j-1]:
    f[i][j] += f[i-1][j-1]        共同往前过一位

solution-fix: 压缩状态至一维数组，需要做反向扫

"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n == 0 or m == 0:
            return 0
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 1
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        return f[n][m]

# ---
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n == 0 or m == 0:
            return 0
        f = [0 for _ in range(m + 1)]
        f[0] = 1
        for i in range(1, n + 1):
            for j in reversed(range(1, m + 1)):
                if s[i - 1] == t[j - 1]:
                    f[j] += f[j - 1]

        return f[m]