"""

link: https://leetcode-cn.com/problems/next-greater-element-i

problem: 求 nums1 中元素 x，在 nums2 中的下一个大于其的值

solution: 字典加搜索。

solution-fix: 单调栈。先预查找 nums2 中每个元素的下一个大于其的值

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

# ---
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, m, res = [], {}, []
        for k in nums2:
            while stack and stack[-1] < k:
                m[stack.pop()] = k
            stack.append(k)
        while stack:
            m[stack.pop()] = -1
        for k in nums1:
            res.append(m[k])
        return res
