"""

link: https://leetcode-cn.com/problems/n-queens

problem: N皇后

solution: 搜就完事了，位运算做加速

"""

class Solution:
    def dfs(self, board: List, cur: int, l: int, res: List[List[int]]):
        def conflict(a, b):
            return a & b != 0

        for i in range(0, l):
            valid = True
            for k in range(0, cur):
                if conflict(board[k], 1 << i) or conflict(board[k], 1 << (i + cur - k)) or (
                        i - cur + k >= 0 and conflict(board[k], 1 << (i - cur + k))):
                    valid = False
                    break
            if valid:
                board[cur] |= 1 << i
                if cur == (l - 1):
                    res.append([t for t in board])
                else:
                    self.dfs(board, cur + 1, l, res)
                board[cur] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [0] * n
        res = []
        self.dfs(board, 0, n, res)
        output = []
        for r in res:
            temp = [''] * n
            for k in range(n):
                for p in range(n):
                    temp[k] += '.' if r[k] & 1 << p == 0 else 'Q'
            output.append(temp)
        return output
