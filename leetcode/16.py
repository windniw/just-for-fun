"""

link: https://leetcode.cn/problems/3sum-closest/ 

problem: 给定数组，求数组中任意三数之和与目标值最接近的值

solution: 排序后，双指针遍历，计算三数之和，更新最接近值

"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(0, len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                x = nums[i] + nums[l] + nums[r]
                if x < target:
                    l += 1
                    res = x if abs(x-target) < abs(res-target) else res
                elif x > target:
                    r -= 1
                    res = x if abs(x-target) < abs(res-target) else res
                else:
                    return x
        return res