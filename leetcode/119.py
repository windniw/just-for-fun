"""

link: https://leetcode.com/problems/triangle

problem: 杨辉三角

solution: 通项公式。

"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [_ for _ in range(rowIndex+1)]
        res[0] = 1
        for i in range(1, rowIndex+1):
            res[i] = res[i-1] * (rowIndex-i+1) // i
        return res
