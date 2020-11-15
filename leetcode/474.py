"""

link: https://leetcode-cn.com/problems/ones-and-zeroes

problem: 数组元素为仅由01组成的字符串，求最大的满足所有元素的0次数小于等于m，1次数小于等于n的子集

solution: DP。二维的01背包问题。

"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        ns, ms = [0 for _ in strs], [0 for _ in strs]
        l = len(strs)
        for i in range(l):
            for k in strs[i]:
                if k == '0':
                    ms[i] += 1
                else:
                    ns[i] += 1

        dp[0][0] = 0
        for wi in range(l):
            for i in range(n, ns[wi] - 1, -1):
                for j in range(m, ms[wi] - 1, -1):
                    if dp[i - ns[wi]][j - ms[wi]] != -1:
                        dp[i][j] = max(dp[i - ns[wi]][j - ms[wi]] + 1, dp[i][j])
        return max(max(a) for a in dp)
