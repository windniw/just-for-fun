"""

link: https://leetcode-cn.com/problems/sparse-matrix-multiplication 

problem: 稀疏矩阵乘法

solution: A[m*p] * B[p*n] = C[m*n]，有 C[i][j] = sum{A[i][k] * B[k][j] | k ∈ [0,p)}

solution-fix: 当矩阵稀疏时，通过特殊处理0值极大优化运行时间。

"""
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, p, n = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    C[i][j] += A[i][k] * B[k][j]
        return C

#---
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, p, n = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(p):
            for i in range(m):
                if A[i][k] == 0:
                    continue
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C
