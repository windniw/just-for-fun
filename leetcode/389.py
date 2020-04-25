"""

link: https://leetcode.com/problems/find-the-difference

problem: s, t 字符串差一个字符，求该字符

solution: 丢进map里统计

"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for k in t:
            m[k] = m[k] + 1 if k in m else 1
        for k in s:
            m[k] = m[k] - 1
        for k in m:
            if m[k] != 0:
                return k
