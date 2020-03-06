"""

link: https://leetcode.com/problems/h-index-ii

problem: 给定升序序列，定义 [h] 为 nums 中精确有 h 个数字，值大于等于h，求[h]的最大值

solution: 二分。若 nums[k] >= n - k, 因为 k 之后的每个数都大于等于 nums[k], 所以肯定有精确 n-k个数字大于 nums[k] >= n-k
          显然，最大的 n-k 值即为 h，二分检索此条件即可

"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r, res = 0, n - 1, 0
        while l <= r:
            mid = (l + r) >> 1
            if citations[mid] >= n - mid:
                res = max(res, n - mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
