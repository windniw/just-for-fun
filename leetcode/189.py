"""

link: https://leetcode.com/problems/rotate-array

problem: 以环形旋转数组

solution: 翻转整个数组，再分别翻转前后两段

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rev(x: List[int], st, en: int):
            ll = en - st
            for i in range(st, st + ll // 2):
                x[i], x[en - 1 - i + st] = x[en - 1 - i + st], x[i]

        l = len(nums)
        k %= l
        rev(nums, 0, l)
        rev(nums, 0, k)
        rev(nums, k, l)
