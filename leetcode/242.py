"""

link: https://leetcode.com/problems/valid-anagram

problem: 判断两字符串字母是否相等

solution: 转map判

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)
        for k in s:
            d1[k] += 1
        for k in t:
            d2[k] += 1
        for k in d1:
            if d1[k] != d2[k]:
                return False
        return True
