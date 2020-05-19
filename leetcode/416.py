"""

link: https://leetcode.com/problems/partition-equal-subset-sum

problem: 问数组能否拆分成两个和相等的集合

solution: 丢集合里存中间可能的和。

solution-fix: 01背包。

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, v = sum(nums), {0}
        for x in nums:
            t = set()
            for k in v:
                c = x + k
                if c * 2 == s:
                    return True
                if c < s // 2 and c not in v:
                    t.add(c)
            v = v.union(t)
        return False

# ---
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for k in nums:
            for i in range(s // 2, 0, -1):
                if i - k >= 0 and dp[i - k]:
                    dp[i] = True
        return dp[s // 2]
