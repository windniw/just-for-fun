"""

link: https://leetcode-cn.com/problems/paint-fence

problem: 用 k 种颜色填 n 个格子，要求相邻三个格子不能同色，求所有的染色总数

solution: DP。f[i][0] 记录与上一个格子不同色的数量，f[i][1] 记录与上一个格子同色的数量。有
            f[i][0] = (f[i - 1][0] + f[i - 1][1]) * (k - 1)    // 对截至 i-1 格的每种染色方案，i 格取与 i-1 不同的 k-1 种颜色
            f[i][1] = f[i - 1][0]                              // 对截至 i-1 格的每种染色方案，i 格与 i-1 格保持同色，方案数相同且肯定合法

"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        f = [[_, _] for _ in range(n)]
        f[0][0], f[0][1] = k, 0
        for i in range(1, n):
            f[i][0] = (f[i - 1][0] + f[i - 1][1]) * (k - 1)
            f[i][1] = f[i - 1][0]
        return f[n - 1][0] + f[n - 1][1]
