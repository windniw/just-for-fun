"""

link: https://leetcode.com/problems/subarray-sum-equals-k

problem: 求数组中是否存在子串满足其和为给定数字，求满足条件子串数。

solution: 记录前缀和。

"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s, cur, res = {0: 1}, 0, 0
        for x in nums:
            if cur + x - k in s:
                res += s[cur + x - k]
            cur += x
            s[cur] = s[cur] + 1 if cur in s else 1
        return res
