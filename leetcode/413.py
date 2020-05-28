"""

link: https://leetcode.com/problems/arithmetic-slices

problem: 求数组的长度的大于3的所有子串中，等差序列的个数

solution: 因为子串必须连续，且若 A[i:j] 与 A[i1:j1] 相交且有相同的公差，A[i:j1] 也为等差序列。
          直接计算所有最长的 A[i:j1]，后计算能从中划分出多少个子序列

"""

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 2:
            return 0
        res, k, t = 0, A[1] - A[0], 2
        for i in range(2, len(A)):
            if k == A[i] - A[i - 1]:
                t += 1
            else:
                res += (t - 1) * (t - 2) // 2
                t = 2
                k = A[i] - A[i - 1]
        res += (t - 1) * (t - 2) // 2
        return res
