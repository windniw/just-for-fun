"""

link: https://leetcode-cn.com/problems/design-tic-tac-toe

problem: a，b 下井字棋，当有人先填满某行某列或对角线时获胜，输入为落子顺序，获胜时返回获胜人，要求时间小于O(n^2)

solution: 位运算优化，时间 O(1)，空间 O(n)，注意可以连续落子

"""
class TicTacToe:

    def __init__(self, n: int):
        class matrix:
            def __init__(self):
                self.row = [0] * n
                self.col = [0] * n
                self.a = 0
                self.b = 0

        self.data = [matrix(), matrix()]
        self.n = n
        self.ok = (1 << n) - 1

    def move(self, row: int, col: int, player: int) -> int:
        m = self.data[player - 1]
        m.row[row] |= 1 << col
        m.col[col] |= 1 << row
        if row == col:
            m.a |= 1 << row
        if row == self.n - 1 - col:
            m.b |= 1 << row
        return player if any([x == self.ok for x in m.row]) or any(
            [x == self.ok for x in m.col]) or m.a == self.ok or m.b == self.ok else 0
