"""

link: https://leetcode.com/problems/surrounded-regions

problem: 对矩阵中除边缘格子外，染色

solution: dfs

"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        n, m = len(board), len(board[0])

        def dfs(i, j):
            if not 0 <= i < n or not 0 <= j < m:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = 'P'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'