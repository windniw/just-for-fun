"""

link: https://leetcode-cn.com/problems/n-queens

problem: N皇后

solution: 搜就完事了，位运算做加速

solution-fix: 递归透传(列，左斜线，右斜线)，可以减少一个for，运行时间少了2/3

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

# ---
class Solution:
    def dfs(self, board: List, raw: int, n: int, col: int, left_line: int, right_line: int, res: List[List[int]]):
        def conflict(a, b):
            return a & b != 0

        for i in range(0, n):
            cur = 1 << i
            if not (conflict(col, cur) or conflict(left_line, cur) or conflict(right_line, cur)):
                board[raw] |= 1 << i
                if raw == (n - 1):
                    res.append([t for t in board])
                else:
                    self.dfs(board, raw + 1, n, col | cur, (left_line | cur) << 1, (right_line | cur) >> 1, res)
                board[raw] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [0] * n
        res = []
        self.dfs(board, 0, n, 0, 0, 0, res)
        output = []
        for r in res:
            temp = [''] * n
            for k in range(n):
                for p in range(n):
                    temp[k] += '.' if r[k] & 1 << p == 0 else 'Q'
            output.append(temp)
        return output
