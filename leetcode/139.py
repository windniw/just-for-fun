"""

link: https://leetcode.com/problems/word-break

problem: 给字符串s，数组list，问s是否能用所有list中的单词组成，无限制次数

solution: 丢进map加缓存扫

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