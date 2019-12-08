"""

link: https://leetcode.com/problems/word-break

problem: 给字符串s，数组list，问s是否能用所有list中的单词组成，无限制次数

solution: 丢进map加缓存扫

solution-fix: DP。定义 dp[i] 为 s[:i] 是否满足条件，枚举dp[i]的断点判断是否可拆为两个单词

"""

import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        for x in wordDict:
            m[x] = True

        @functools.lru_cache(maxsize=None)
        def dfs(ss: str):
            if ss == "":
                return True
            for i in range(len(ss)):
                if ss[:i+1] in m:
                    if dfs(ss[i+1:]):
                        return True
            return False

        return dfs(s)

#---
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        for x in wordDict:
            m[x] = True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in m:
                    dp[i] = True
                    break
        return dp[len(s)]