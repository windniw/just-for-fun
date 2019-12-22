"""

link: https://leetcode.com/problems/excel-sheet-column-title

problem: 26 进制

solution: 从 1 开始的26进制，每轮计算时记得退一

"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n != 0:
            n -= 1
            res = chr(65 + n % 26) + res
            n = n // 26
        return res
