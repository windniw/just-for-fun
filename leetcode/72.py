"""

link: https://leetcode.com/problems/edit-distance

problem: 给定两个字符串，定义三种操作 删除/插入/替换 单个字符，问A最少经过多少次操作可变为B

solution: DP。定义dp[i][j]=minDistance(word1[:i],word2[:j]) 注意dp[0][0]代表的是("","")，而不是(word1[0],word2[0])
有以下转移方程 dp[i][j] = min(
                dp[i-1][j-1] / dp[i-1][j-1] + 1,  // 最后两位相同do nothing / 最后两位不同，替换 word1[i] --> word2[j]
                dp[i-1][j] + 1,                   // 删除 word1[i]
                dp[i][j-1] + 1                    // 增加 word2[j]
              )  

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if n + m == 0: return max(n, m)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            dp[0][i] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]