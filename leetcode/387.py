"""

link: https://leetcode.com/problems/first-unique-character-in-a-string

problem: 求字符串中的第一个不重复字符位置

solution: 丢进map里统计

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            x = s[i]
            m[x] = i if x not in m else -1
        res = len(s)
        for x in m:
            res = min(res, m[x]) if m[x] != -1 else res
        return -1 if res == len(s) else res
