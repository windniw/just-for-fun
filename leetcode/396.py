"""

link: https://leetcode.com/problems/rotate-function

problem: 定义 F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1], 其中 Bk 为 A 的顺时针旋转k，求F(k)的最大值 

solution: DP。显然F(k)间存在递推关系 F(k) = F(k-1) + sum(A) - A[n-1-k] * n

"""
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        f = sum([i * x for i, x in enumerate(A)])
        res, s, n = f, sum(A), len(A)
        for i in range(n):
            res = max(res, f)
            f = f + s - A[n - 1 - i] * n
        return res
