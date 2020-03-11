"""

link: https://leetcode.com/problems/game-of-life

problem: 01 矩阵，若 1 的相邻 1 少于2或多于3 则变 0，若 0 的相邻 1 等于3 则变 1，要求空间O(1)

solution: 因为是一次性检查，所以不可能不适用额外空间来检查扫描过的格子，但要求空间O(1)，只能在每个已有格子上做文章。
          注意到 01 矩阵，使用奇偶性来记录原格子的值，每次 +2 即可通过最低位知道格子原值是多少，最后再扫回去即可。

solution-fix：思路同上。除了奇偶，还可以通过划分位来扩大空间，用最低位记录原值，用更高位来记录相邻的数量。

"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                board[i][j] += (board[i - 1][j - 1] & 1) * 2 if i > 0 and j > 0 else 0
                board[i][j] += (board[i - 1][j] & 1) * 2 if i > 0 else 0
                board[i][j] += (board[i - 1][j + 1] & 1) * 2 if i > 0 and j < m - 1 else 0
                board[i][j] += (board[i][j - 1] & 1) * 2 if j > 0 else 0
                board[i][j] += (board[i][j + 1] & 1) * 2 if j < m - 1 else 0
                board[i][j] += (board[i + 1][j - 1] & 1) * 2 if i < n - 1 and j > 0 else 0
                board[i][j] += (board[i + 1][j] & 1) * 2 if i < n - 1 else 0
                board[i][j] += (board[i + 1][j + 1] & 1) * 2 if i < n - 1 and j < m - 1 else 0
        for i in range(n):
            for j in range(m):
                live = board[i][j] & 1
                cnt = board[i][j] // 2
                if live and cnt < 2 or cnt > 3:
                    live = False
                elif not live and cnt == 3:
                    live = True
                board[i][j] = 1 if live else 0
