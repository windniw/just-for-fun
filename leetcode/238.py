"""

link: https://leetcode.com/problems/product-of-array-except-self

problem: 返回res，对res[i] = nums[:i] * nums[i+1:]，要求时间O(n)，空间O(1)，不允许用除法

solution: 时间O(n)，空间O(n)，用两个数组预先算好左右扫描的乘积

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]
        r1, r2, res = [1 for _ in range(n)], [1 for _ in range(n)], [_ for _ in range(n)]
        r1[0], r2[-1] = nums[0], nums[-1]
        for i in range(1, n):
            r1[i] = nums[i] * r1[i - 1]
            r2[n - 1 - i] = nums[n - 1 - i] * r2[n - i]
        res[0], res[n - 1] = r2[1], r1[n - 2]
        for i in range(1, n - 1):
            res[i] = r1[i - 1] * r2[i + 1]
        return res
