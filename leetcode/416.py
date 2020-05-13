"""

link: https://leetcode.com/problems/partition-equal-subset-sum

problem: 问数组能否拆分成两个和相等的集合

solution: 丢集合里存中间可能的和。

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
