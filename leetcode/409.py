
"""

link: https://leetcode.com/problems/longest-palindrome

problem: 问用s中字符组成的最长回文串长度

solution: map 记录字符出现次数

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m, res = collections.defaultdict(int), 0
        for x in s:
            m[x] += 1
        for x in m:
            res += m[x] // 2 * 2
        return min(len(s), res + 1)

