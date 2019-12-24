"""

link: https://leetcode.com/problems/excel-sheet-column-number

problem: 字符转数字，26进制

solution: 按位累加

"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for x in s:
            res = res * 26 + (ord(x) - ord('A') + 1)
        return res