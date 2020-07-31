"""

link: https://leetcode-cn.com/problems/paint-house-ii

problem: 给 n*k 的数组，每项选一个数字，相邻选中的列数不能一致，求最小和，要求时间复杂O(nk)

solution: DP。dp状态很清晰，dp[i][j] 表示选到第 i 行时，选中第 j 项的当前最小和，显然有
          dp[i][j] = min(min(dp[i-1][:j]), min(dp[i-1][j+1:]))，区别只是填表的方式。
          O(nkk)的思路很容易想到，每次遍历 dp[i-1] 的每一项找到最小值，每项花时间是O(k)。在这里做个优化，左右各扫一轮记录
          left[:j], right[j:] 的最小值，即可优化到O(1)，总时间即为 O(nk)。加滚动数组做压缩。
        
solution: 只记录 dp[i-1] 的最小值和第二小值即可，当与最小值相等时取第二小。

"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not len(costs) or not len(costs[0]):
            return 0
        n, k = len(costs), len(costs[0])
        if len(costs[0]) == 1:
            return sum([costs[i][0] for i in range(n)])
        
        dp = [costs[0][i] for i in range(k)]
        left, right = [_ for _ in range(k)], [_ for _ in range(k)]
        for i in range(1, n):
            for j in range(k):
                left[j] = dp[j] if j == 0 else min(left[j - 1], dp[j])
            for j in reversed(range(k)):
                right[j] = dp[j] if j == k - 1 else min(right[j + 1], dp[j])
            dp[0], dp[k - 1] = right[1] + costs[i][0], left[k - 2] + costs[i][k - 1]
            for j in range(1, k - 1):
                dp[j] = min(left[j - 1], right[j + 1]) + costs[i][j]
        return min(dp)

# ---
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not len(costs) or not len(costs[0]):
            return 0
        n, k = len(costs), len(costs[0])
        if len(costs[0]) == 1:
            return sum([costs[i][0] for i in range(n)])

        dp = [costs[0][i] for i in range(k)]
        for i in range(1, n):
            fm, sm = dp[0], float("inf")
            for j in range(1, k):
                if dp[j] <= fm:
                    sm = fm
                    fm = dp[j]
                elif dp[j] < sm:
                    sm = dp[j]
            for j in range(0, k):
                dp[j] = (fm if dp[j] != fm else sm) + costs[i][j]
        return min(dp)
