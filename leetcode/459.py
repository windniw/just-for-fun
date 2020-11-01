"""

link: https://leetcode-cn.com/problems/repeated-substring-pattern

problem: 问字符串s中是否存在自循环

solution: 双倍字符。若s中存在循环节，则 ss 中，从第一位（注意不是第0位）第一次出现s的位置，必然不是第二个s的位置。

"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
