"""

link: https://leetcode.com/problems/pascals-triangle

problem: 杨辉三角

solution: 模拟。

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        for i in range(numRows):
            res[i] = [_ for _ in range(i + 1)]
            res[i][0] = 1
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
            res[i][i] = 1
        return res
