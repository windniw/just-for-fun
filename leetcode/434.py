"""

link: https://leetcode.com/problems/number-of-segments-in-a-string

problem: 求字符串中单词数量

solution: split

"""
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())