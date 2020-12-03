"""

link: https://leetcode-cn.com/problems/split-array-largest-sum

problem: 将 nums 分割成 m 个连续子串，求所有分割方式中，子串集最大值的最小值

solution: 二分。计算分割状态复杂度很高，可以反过来考虑，假设给定解为 x，可以在 O(n) 的时间复杂度内检查nums是否有该解。
          所以可以二分枚举解，时间复杂为 O(log(sum(nums)) * n)

"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def f(x: int) -> bool:
            c, cnt = 0, 0
            for i in nums:
                if c + i > x:
                    cnt += 1
                    c = i
                else:
                    c += i
            return cnt + 1 <= m

        i, j  = max(nums), sum(nums)
        res = j
        while i < j:
            mid = (i + j) >> 1
            if f(mid):
                res = min(res, mid)
                j = mid
            else:
                i = mid + 1
        return res