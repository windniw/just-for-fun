"""

link: https://leetcode.com/problems/palindrome-partitioning

problem: 将字符串s分割成若干回文子串，求所有可能

solution: 搜索

"""
import functools 

class Solution:
    @functools.lru_cache(maxsize=None)
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        res = []

        def f(ss: str) -> bool:
            for i in range((len(ss) + 1) // 2):
                if ss[i] != ss[-1 - i]:
                    return False
            return True

        for i in range(len(s)):
            if f(s[:i + 1]):
                t = self.partition(s[i + 1:])
                for x in t:
                    tt = [s[:i + 1]]
                    tt = tt + x
                    res.append(tt)
        return res