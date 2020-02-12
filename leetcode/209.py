"""

link: https://leetcode.com/problems/minimum-size-subarray-sum

problem: 查找数组中满足 sum[l,r) >=k 中的 min(r-l)

solution: 双指针遍历，时间复杂度O(n)

"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        l, r, k, res = 0, 0, 0, n + 1
        while r < n:
            while k < s and r < n:
                k += nums[r]
                r += 1
            while k >= s:
                res = min(res, r - l)
                if res == 1:
                    return 1
                k -= nums[l]
                l += 1
        return res if res != n + 1 else 0
