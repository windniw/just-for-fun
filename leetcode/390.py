"""

link: https://leetcode.com/problems/elimination-game

problem: 对 [1, n] 的序列，每次从左向右间隔一位删数，再从右向左间隔一位删数，求最后剩下的数字

solution: 模拟倒推。已知最后一次时，该剩下数字在数列中位置为1，自底向上推到起始时的数字位置。

"""
class Solution:
    def lastRemaining(self, n: int) -> int:
        def f(num: int) -> int:
            return 1 if num == 1 else num - f(num // 2) * 2 + 1

        return n - f(n) + 1
