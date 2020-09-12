"""

link: https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k

problem: 求数组中最长子数组，满足其和为 k，子数组必然连续。时间O(n)

solution: 遍历时记录 sum(nums[:i+1]) 的首次出现位置，并检查 sum(nums[:i+1]) - k 是否在之前出现过，
          若有，记该值对应位置 j，[j:i+1] 为一个满足条件的子数组 

"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        m, t, res = {}, 0, 0
        for i, v in enumerate(nums):
            t += v
            if t not in m:
                m[t] = i
            if t == k:
                res = i + 1
            elif t - k in m:
                res = max(i - m[t - k], res)
        return res
