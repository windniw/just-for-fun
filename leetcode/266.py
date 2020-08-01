"""

link: https://leetcode-cn.com/problems/palindrome-permutation

problem: 问给定字符串重新组合后能否回文

solution: map记录，检查所有字符中奇数次数的数量是否小于2
       
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = collections.defaultdict(int)
        for x in s:
            m[x] += 1
        return sum([(m[x] & 1) for x in m]) < 2
