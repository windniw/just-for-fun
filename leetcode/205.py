"""

link: https://leetcode.com/problems/isomorphic-strings

problem: 判断两个字符串是否同构

solution: 按要求转换

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        d1, d2 = collections.defaultdict(str), collections.defaultdict(str)
        for i in range(n):
            if s[i] in d1 or t[i] in d2:
                if not (d1[s[i]] == t[i] and d2[t[i]] == s[i]):
                    return False
            else:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
        return True
