"""

link: https://leetcode-cn.com/problems/count-of-range-sum

problem: 给整数数组，求统计有多少区间和位于 [lower, upper] 间，要求时间复杂度优于 O(n^2)

solution: 前缀和 + 二分。python 没有现成的平衡树结构，用二分来实现上下限的查找。

"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        t = [_ for _ in nums]
        for i, v in enumerate(nums):
            t[i] = nums[0] if i == 0 else t[i - 1] + nums[i]
        t.sort()
        res, p = 0, 0
        for i in range(len(nums)):

            def f_upper(k: int):
                l, r = 0, len(t) - 1
                while l < r:
                    mid = (l + r) >> 1
                    if t[mid] <= k:
                        l = mid + 1
                    else:
                        r = mid
                return l

            def f_lower(k: int):
                l, r = 0, len(t) - 1
                while l < r:
                    mid = (l + r) >> 1
                    if t[mid] >= k:
                        r = mid
                    else:
                        l = mid + 1
                return l

            l, r = f_lower(lower + p), f_upper(upper + p)
            if t[r] <= upper + p:
                r += 1
            if t[l] < lower + p:
                l += 1
            res += r - l
            p += nums[i]
            t.pop(f_lower(p))
        return res