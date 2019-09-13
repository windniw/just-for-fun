"""

link: https://leetcode.com/problems/wildcard-matching/

problem: 问类正则表达式p是否能完全匹配s，其中p的匹配规则为 * -> 0+ any chars && ? -> 1 any char

solution: DP，定义 dp[i][j] 为s[:i]是否匹配p[:j]，注意是dp[0][0]代表空字符串和空正则允许匹配
初始化dp[0][k]后分情况讨论即可(注意实际代码为了方便处理，将s，p均右移了一位)：
dp[i][j] = (p[j] == '*' && dp[i][j-1])                    # '*' 匹配空值
         = (p[j] == '*' && dp[i-1][j])                    # '*' 匹配1+个任意字符
         = (p[j] == '*' && dp[i-1][j-1])                  # '*' 匹配1个任意字符
         = (p[j] == '?' || s[i] == p[j] && dp[i-1][j-1])  # ? 或其他字符精确匹配

solution-fix: 剪枝搜索，"*" 是个很神奇的匹配，可以将模式串抽象成 p1*p2*p3*p4 这样的序列，多个连续"*"
可以合并成一个，这时只需要确认s存在子序列 p1p2p3p4 即可
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

# ---

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, confirm_j, pre_i = 0, 0, 0, 0
        while not (i == len(s) and j == len(p)):
            if i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                j += 1
                pre_i = i
                confirm_j = j
            else:
                if confirm_j == 0 or pre_i >= len(s):
                    return False
                j = confirm_j
                i = pre_i + 1
                pre_i = i
        while j < len(p) and p[j] == '*':
            j += 1
        return i == len(s) and j == len(p)
