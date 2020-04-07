"""

link: https://leetcode.com/problems/integer-break

problem: 将n拆分成若干个整数之和，求这堆整数的最大积，2 <= n <= 58

solution: DP。dp[i] 为 n==i 时的最优解，遍历所有组合可能即可

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(dp[j], j) * max(dp[i - j], i - j))

        return dp[n]
