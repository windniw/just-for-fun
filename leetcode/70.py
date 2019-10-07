"""

link: https://leetcode.com/problems/climbing-stairs

problem: 对n阶楼梯，每次可走1或2阶，问登顶路径数

solution: 斐波那契序列

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [_ for _ in range(n + 1)]
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]