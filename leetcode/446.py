"""

link: https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence

problem: 求所有数组所有子序列中的等差子序列数量，子序列长度大于等于3

solution: DP。记 f[i][j] 为以 i 为首位的子序列中，公差为 j 的子序列数量，这里包括长度为 2 的子序列，但注意长度
          为 2 的子序列不记入最终结果。有 f[i][j] = sum(f[k][j]) + count(A[kk]) | k ∈ [i+1, n), A[kk] = A[i] + j

"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        n, cnt = len(A), 0
        f = [{} for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if d not in f[i]:
                    f[i][d] = 0
                f[i][d] += 1
                if d in f[j]:
                    f[i][d] = f[i][d] + f[j][d]
                    cnt += f[j][d]
        return cnt
