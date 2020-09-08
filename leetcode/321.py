"""

link: https://leetcode-cn.com/problems/create-maximum-number

problem: 在两个数字数组中共挑选 k 个数，要求其结果最大，且每个数组中挑出来的数字，在最终结果中顺序相同。

solution: 枚举分别在数组中挑选 (0, k), (1, k-1) ... (k, 0) 个数字，用单调栈寻找最大结果且合并，从中找出最大值。
          注意 select 得到的数组并非绝对有序（当 k 较大而 n 较小的情况），所以在 merge 时不能用正常的归并排序思路
          只比较首位，每次必须比较整个数组。

"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def select(nums: List[int], kk: int):
            stack, n = [], len(nums)
            for i, v in enumerate(nums):
                while stack and stack[-1] < v and len(stack) + n - i > kk:
                    stack.pop()
                stack.append(v)
            return stack[:kk]

        def merge(n1, n2) -> List[int]:
            res = []
            while n1 or n2:
                t = n1 if n1 > n2 else n2
                res.append(t[0])
                t.pop(0)
            return res

        res = []
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, merge(select(nums1, i), select(nums2, k - i)))
        return res
