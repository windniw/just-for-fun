"""

link: https://leetcode.com/problems/n-queens-ii

problem: N皇后

solution: 搜就完事了，同51，去掉结构化部分

"""

class Solution:
    def dfs(self, raw: int, n: int, col: int, left_line: int, right_line: int):
        def conflict(a, b):
            return a & b != 0

        res = 0
        for i in range(0, n):
            cur = 1 << i
            if not (conflict(col, cur) or conflict(left_line, cur) or conflict(right_line, cur)):
                if raw == (n - 1):
                    return 1
                else:
                    res += self.dfs(raw + 1, n, col | cur, (left_line | cur) << 1, (right_line | cur) >> 1)
        return res

    def totalNQueens(self, n: int) -> int:
        return self.dfs(0, n, 0, 0, 0)
