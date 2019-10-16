"""

link: https://leetcode.com/problems/word-search

problem: 给二维数组，求路径满足word

solution: DFS搜

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0: return False
        n, m = len(board), len(board[0])
        visit = [[False] * m for _ in range(n)]

        def dfs(i, j, k: int) -> bool:
            if k == len(word): return True
            if i > 0 and not visit[i - 1][j] and board[i - 1][j] == word[k]:
                visit[i - 1][j] = True
                if dfs(i - 1, j, k + 1): return True
                visit[i - 1][j] = False

            if i < n - 1 and not visit[i + 1][j] and board[i + 1][j] == word[k]:
                visit[i + 1][j] = True
                if dfs(i + 1, j, k + 1): return True
                visit[i + 1][j] = False

            if j > 0 and not visit[i][j - 1] and board[i][j - 1] == word[k]:
                visit[i][j - 1] = True
                if dfs(i, j - 1, k + 1): return True
                visit[i][j - 1] = False

            if j < m - 1 and not visit[i][j + 1] and board[i][j + 1] == word[k]:
                visit[i][j + 1] = True
                if dfs(i, j + 1, k + 1): return True
                visit[i][j + 1] = False

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visit[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    visit[i][j] = False
        return False