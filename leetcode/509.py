"""

link: https://leetcode-cn.com/problems/fibonacci-number

problem: 斐波那契， n <= 30

solution: 递推

"""
class Solution:
    def fib(self, n: int) -> int:
        f = [0 for _ in range(31)]
        f[0], f[1] = 0, 1
        for i in range(2, n + 1):
            f[i] = f[i - 2] + f[i - 1]
        return f[n]
