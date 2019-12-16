"""

link: https://leetcode.com/problems/maximum-product-subarray

problem: 求子串的最大乘积，可能包含非正数，子串不能为空

solution: DP。dp_min[i] 为以 nums[i] 为结尾的子串的最小值 ，dp_max 类同。
          想象纯正数的情况，dp_max[i] = dp_max[i-1] * nums[i]；
          再增加负数的情况，需要维护最小值，当其为负且nums[i]为负时，min_res * x 可能变为最大值，有
          dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])；
          最后考虑0值，当出现0时，正数负数都没意义，有
          dp_max[i] = 0, dp_min = 0。
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_res, max_res, res = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            t = max_res
            max_res = max(x, max_res * x, min_res * x)
            min_res = min(x, min_res * x, t * x)
            res = max(res, max_res)
        return res
