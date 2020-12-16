"""

link: https://leetcode-cn.com/problems/encode-string-with-shortest-length

problem: 尽可能压缩字符串

solution: DP。请结合 #459 来看。令 dp[i][j] 代表 s[i:j+1] 的最短编码，则有 
          if s[i:j+1] 存在循环节, dp[i][j] = "cnt[x]" | cnt 为循环节出现次数，x 为循环节
          else dp[i][j] = min_len(dp[i][k] + dp[k+1][j]) | k ∈ [i, j-1]
          其中状态总数 O(n^2), 状态转移时间复杂度 O(n)，检查某字符串 s 是否存在循环节时间负责度 O(find)
          总的时间复杂度为 O(n^3 * O(str.find))

"""
class Solution:
    def encode(self, s: str) -> str:
        if not s:
            return ""

        def f(x: str) -> int:
            t = (x + x).find(x, 1)
            return -1 if t == len(s) else t

        n = len(s)
        dp = [["" for _ in range(n)] for _ in range(n)]
        for i in reversed(range(n)):
            dp[i][i] = s[i]
            for j in range(i + 1, n):
                t = f(s[i:j + 1])
                if t != -1 and t + 3 < j - i + 1:
                    dp[i][j] = str((j + 1 - i) // t) + '[' + dp[i][i + t - 1] + ']'
                    continue
                for k in range(i, j):
                    if dp[i][j] == "" or len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k + 1][j]
        return dp[0][n - 1]
