"""

link: https://leetcode.com/problems/permutations-ii

problem: 求全排列，nums中存在重复数

solution: 同46，加上排序即可

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        new_nums = nums.copy()
        new_nums.sort()
        res = []
        for i in range(0, len(new_nums)):
            if i + 1 < len(new_nums) and new_nums[i] == new_nums[i + 1]:
                continue
            new_nums[i], new_nums[0] = new_nums[0], new_nums[i]
            sub_result = self.permuteUnique(new_nums[1:])
            for r in sub_result:
                res.append([new_nums[0]] + r.copy())
            new_nums[i], new_nums[0] = new_nums[0], new_nums[i]
        return res
