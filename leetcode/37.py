"""

link: https://leetcode.com/problems/sudoku-solver

problem: 解数独

solution: 写搜索真是练手良方。。。先算好每行、列、块出现过的数字预剪枝；
          再做DFS，每次预填刷新该格子的行列块数字，失败再刷回来

"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = []
        for i in range(9):
            s = 0
            for j in range(9):
                if board[i][j] != '.':
                    s |= 1 << (ord(board[i][j]) - 48)
            row.append(s)

        col = []
        for i in range(9):
            s = 0
            for j in range(9):
                if board[j][i] != '.':
                    s |= 1 << (ord(board[j][i]) - 48)
            col.append(s)

        block = []
        for i in range(9):
            s = 0
            for j1 in range(3):
                for j2 in range(3):
                    if board[(i // 3) * 3 + j1][(i % 3) * 3 + j2] != '.':
                        s |= 1 << (ord(board[(i // 3) * 3 + j1][(i % 3) * 3 + j2]) - 48)
            block.append(s)

        self.dfs(board, row, col, block, 0, 0)

    def dfs(self, board: List[List[str]], row: [int], col: [int], block: [int], p1, p2: int) -> bool:
        if p2 == 9: p1 += 1;p2 = 0
        while p1 != 9 and board[p1][p2] != '.':
            p2 += 1
            if p2 == 9: p1 += 1;p2 = 0

        if p1 == 9: return True

        t = row[p1] | col[p2] | block[p1 // 3 * 3 + p2 // 3]
        for k in range(1, 10):
            if t & (1 << k) == 0:
                row[p1] |= 1 << k
                col[p2] |= 1 << k
                block[p1 // 3 * 3 + p2 // 3] |= 1 << k
                if self.dfs(board, row, col, block, p1, p2 + 1):
                    board[p1][p2] = chr(48 + k)
                    return True
                row[p1] &= ~ (1 << k)
                col[p2] &= ~ (1 << k)
                block[p1 // 3 * 3 + p2 // 3] &= ~ (1 << k)
        return False