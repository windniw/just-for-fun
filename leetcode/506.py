"""

link: https://leetcode-cn.com/problems/relative-ranks

problem: 求数组每个元素排序后的次序

solution: 排序后记录

"""
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = [_ for _ in nums]
        for i, v in enumerate(nums):
            nums[i] = (-v, i)
        nums.sort()
        for i, k in enumerate(nums):
            if i == 0:
                res[k[1]] = "Gold Medal"
            elif i == 1:
                res[k[1]] = "Silver Medal"
            elif i == 2:
                res[k[1]] = "Bronze Medal"
            else:
                res[k[1]] = str(i+1)
        return res
