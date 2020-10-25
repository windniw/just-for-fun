"""

link: https://leetcode-cn.com/problems/find-all-duplicates-in-an-array

problem: 数组元素满足 a[i] ∈ [1, n]，其中有些元素出现两次，有些一次，要求时间O(n)，空间O(1)筛出两次的元素

solution: 利用原数组取相反数作为 visit 数组，扫一遍。

"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for k in nums:
            x = abs(k)
            if nums[x - 1] < 0:
                res.append(x)
            else:
                nums[x - 1] = -nums[x - 1]
        return res
