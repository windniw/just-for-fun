"""

link: https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k

problem: 给矩阵 matrix，求其所有子矩阵和最大且不大于k的值，矩阵行明显大于列

solution: 枚举子矩阵的列端点，将其中行压缩成一维，将问题转换为求一维数组的子串和最大且不大于k
          从左向右扫，维护前缀和，二分搜索 cur - k 是否在前缀和数组内

"""
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        res = float("-inf")
        for i in range(m):
            sum_list = [0] * n
            for j in range(i, m):
                for l in range(n):
                    sum_list[l] += matrix[l][j]
                t, visit = 0, [0]
                for s in sum_list:
                    t += s
                    p = bisect.bisect_left(visit, t - k)
                    if p < len(visit):
                        res = max(res, t - visit[p])
                    bisect.insort_left(visit, t)
        return res