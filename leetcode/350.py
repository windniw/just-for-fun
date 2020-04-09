"""

link: https://leetcode.com/problems/intersection-of-two-arrays-ii

problem: 求两个数组交集

solution: map存出现数量

"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = collections.defaultdict(int)
        for x in nums1:
            m[x] += 1
        for x in nums2:
            if x in m and m[x] != 0:
                res.append(x)
                m[x] = m[x] - 1
        return res
