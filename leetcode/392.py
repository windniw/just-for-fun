"""

link: https://leetcode.com/problems/is-subsequence

problem: 问 s 是否为 t 的子序列

solution: 贪心。对 s 的每位取其在 t 的最前值。

"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in s:
            while i < len(t) and t[i] != x:
                i += 1
            if i == len(t):
                return False
            i += 1
        return True
