"""

link: https://leetcode.com/problems/optimal-division

problem: 给正整数数字数组，默认相除，添加任意括号使得表达式值最大。

solution: 递归枚举分割点。

solution-fix: 注意到对所有元素均为正整数，越除肯定越小。有 a/(b/c) > (a/b)/c，
              即被除数的最大值一定为nums[0], 除数的最小值为nums[1:]的连除

"""
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        def f_max(nums: List[int], req_max: bool):
            if len(nums) == 1:
                return nums[0], str(nums[0])
            t = float("-inf") if req_max else float("inf")
            s1, s2 = "", ""
            for i in range(len(nums) - 1):
                tt1, ss1 = f_max(nums[:i + 1], req_max)
                tt2, ss2 = f_max(nums[i + 1:], not req_max)
                if (t < tt1 / tt2) == req_max:
                    t = tt1 / tt2
                    s1 = ss1
                    s2 = ss2
            return t, s1 + "/" + s2 if "/" not in s2 else s1 + "/" + "(" + s2 + ")"

        _, t = f_max(nums, True)
        return t

# ---
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(k) for k in nums]
        if len(nums) == 1 or len(nums) == 2:
            return "/".join(nums)
        return nums[0] + "/" + "(" + "/".join(nums[1:]) + ")"
