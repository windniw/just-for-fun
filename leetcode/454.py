"""

link: https://leetcode-cn.com/problems/4sum-ii

problem: 给 A, B, C, D 四个等长数组，问共有多少元组 (i, j, k, l) 满足 A[i]+B[j]+C[k]+D[l] == 0，数组长度小于 500

solution: 枚举。预计算 AB / CD 各自两个数组元素的所有可能和存进 dict，再扫一遍查相反数。

"""
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A:
            return 0

        def f(a, b):
            m = collections.defaultdict(int)
            for i in a:
                for j in b:
                    m[i + j] += 1
            return m

        m1, m2, res = f(A, B), f(C, D), 0
        for k, v in m1.items():
            res += v * m2[-k]
        return res
