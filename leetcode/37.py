"""

link: https://leetcode.com/problems/sudoku-solver

problem: 解数独

solution: 写搜索真是练手良方。。。先算好每行、列、块出现过的数字预剪枝；
          再做DFS，每次预填刷新该格子的行列块数字，失败再刷回来

solution-fix: 合并初始项，预先算好待填位置，修改位运算为集合，从 140ms 跑到了 88ms

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

# --- 
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        ss = set('123456789')
        row, col, block, empty = [set() for _ in range(9)], [set() for _ in range(9)], \
                                 [set() for _ in range(9)], []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[i // 3 * 3 + j // 3].add(board[i][j])

        def dfs(p: int) -> bool:
            if p == len(empty): return True

            p1, p2 = empty[p][0], empty[p][1]

            t = row[p1].union(col[p2]).union(block[p1 // 3 * 3 + p2 // 3])
            for k in ss:
                if k not in t:
                    row[p1].add(k)
                    col[p2].add(k)
                    block[p1 // 3 * 3 + p2 // 3].add(k)
                    if dfs(p + 1):
                        board[p1][p2] = k
                        return True
                    row[p1].remove(k)
                    col[p2].remove(k)
                    block[p1 // 3 * 3 + p2 // 3].remove(k)
            return False

        dfs(0)
