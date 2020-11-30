"""

link: https://leetcode-cn.com/problems/next-greater-element-i

problem: 求 nums1 中元素 x，在 nums2 中的下一个大与其的值

solution: 字典加搜索。

"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        m = {v: i for i, v in enumerate(nums2)}
        res = []
        for v in nums1:
            for j in range(m[v] + 1, n + 1):
                if j == n:
                    res.append(-1)
                elif nums2[j] > v:
                    res.append(nums2[j])
                    break
        return res
