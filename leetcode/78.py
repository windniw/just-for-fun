"""

link: https://leetcode.com/problems/subsets

problem: 给不重复数组nums，求其全部子集

solution: 77基础上改改完事

solution-fix: 逐个加数字的思路，在之前序列每种组合上，copy一份并增加新的数字

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def c(keys: [int], m: int) -> List[List[int]]:
            if m == 1: return [[i] for i in keys]
            t = []
            for i in range(0, len(keys) + 1 - m):
                for sub_res in c(keys[i + 1:], m - 1):
                    t.append([keys[i]] + sub_res)
            return t

        res = [[]]
        nums.sort()
        for k in range(1, len(nums) + 1):
            res += (c(nums, k))
        return res

# --- 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + j for j in res]
        return res
