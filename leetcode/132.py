"""

link: https://leetcode.com/problems/palindrome-partitioning-ii

problem: 将字符串s分割成若干回文子串，求最少步数

solution: DP。令dp[i]为s[:i]的最少步数，dp[i] = min(dp[j]+1 if s[j:i] 为回文)。
          做简单优化
          - 若dp[j]+1<=dp[i]，则无需计算子串是否回文
          - 倒序查找j，令dp[i]更早得到极值

"""
class Solution:
    def minCut(self, s: str) -> int:
        if s == '':
            return 0
        def f(ss: str) -> bool:
            for i in range(len(ss) // 2):
                if ss[i] != ss[-1 - i]:
                    return False
            return True

        l = len(s)
        dp = [float("inf") for _ in range(l + 1)]
        dp[0] = 0
        for i in range(l + 1):
            for j in reversed(range(i)):
                if dp[j] + 1 >= dp[i]:
                    continue
                if f(s[j:i]):
                    dp[i] = dp[j] + 1
        return dp[l] - 1