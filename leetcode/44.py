"""

link: https://leetcode.com/problems/wildcard-matching/

problem: 问类正则表达式p是否能完全匹配s，其中p的匹配规则为 * -> 0+ any chars && ? -> 1 any char

solution: DP，定义 dp[i][j] 为s[:i]是否匹配p[:j]，注意是dp[0][0]代表空字符串和空正则允许匹配
初始化dp[0][k]后分情况讨论即可(注意实际代码为了方便处理，将s，p均右移了一位)：
dp[i][j] = (p[j] == '*' && dp[i][j-1])                    # '*' 匹配空值
         = (p[j] == '*' && dp[i-1][j])                    # '*' 匹配1+个任意字符
         = (p[j] == '*' && dp[i-1][j-1])                  # '*' 匹配1个任意字符
         = (p[j] == '?' || s[i] == p[j] && dp[i-1][j-1])  # ? 或其他字符精确匹配
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for i in range(lp+1)] for j in range(ls+1)]
        s, p = '*' + s, '*' + p
        dp[0][0] = True
        for i in range(1, lp+1):
            if p[i] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if ((dp[i][j - 1] or dp[i - 1][j] or dp[i - 1][j - 1]) and p[j] == '*') or \
                        (dp[i - 1][j - 1] and (p[j] == '?' or s[i] == p[j])):
                    dp[i][j] = True
        return dp[ls][lp]
