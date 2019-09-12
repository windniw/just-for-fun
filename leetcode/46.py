"""

link: https://leetcode.com/problems/permutations

problem: 求全排列

solution: 递归即可

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(0, len(nums)):
            nums[i], nums[0] = nums[0], nums[i]
            sub_result = self.permute(nums[1:])
            for r in sub_result:
                res.append([nums[0]] + r.copy())
            nums[i], nums[0] = nums[0], nums[i]
        return res
