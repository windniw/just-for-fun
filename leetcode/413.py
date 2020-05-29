"""

link: https://leetcode.com/problems/arithmetic-slices

problem: 求数组的长度的大于3的所有子串中，等差序列的个数

solution: 因为子串必须连续，且若 A[i:j] 与 A[i1:j1] 相交且有相同的公差，A[i:j1] 也为等差序列。
          直接计算所有最长的 A[i:j1]，后计算能从中划分出多少个子序列

solution-fix: DP。没有更优，只是换个思路。令 dp[i] 为以 A[i] 结尾的合法序列数量，显然有
              dp[i] = A[i] - A[i - 1] == A[i - 1] - A[i - 2] ? dp[i-1] + 1: 0，若跟之前序列等差，
              在之前基础上继续补长，反之重新开始。

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

# ---
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(2, n):
            dp[i] = dp[i - 1] + 1 if A[i] - A[i - 1] == A[i - 1] - A[i - 2] else 0
        return sum(dp)
