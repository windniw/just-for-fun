"""

link: https://leetcode.com/problems/battleships-in-a-board

problem: 给矩阵，数其中连续的X有多少块，每块均为 1*n 或 n*1 的矩阵
         要求只扫一次，空间O(1)，不改变原有矩阵值

solution: 由于不会有不合法输入，只统计每块左上角即可

"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        n, m, res = len(board), len(board[0]), 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and not (i > 0 and board[i - 1][j] == 'X') and not (
                        j > 0 and board[i][j - 1] == 'X'):
                    res += 1
        return res
