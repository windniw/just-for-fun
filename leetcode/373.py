"""

link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums

problem: 用 nums1, nums2 中元素组成元素对 (u,v), 其中 u ∈ nums1，v ∈ nums2，求所有元素对中和最小的前 k 对

solution: 小根堆。因为 (nums[i], nums[j]) < (nums[i], nums[j+1])，可以肯定前者未出堆时后者入堆也没有意义，在前者出堆再将后者入堆
          保持堆大小为 n，而不需要 mn，时间复杂度（klogn）

"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        class T:
            def __init__(self, a: int, b: int, i: int):
                self.a = a
                self.b = b
                self.i = i

            def __lt__(self, t):
                return self.a + self.b < t.a + t.b

        if not nums1 or not nums2:
            return []

        n, m = len(nums1), len(nums2)

        h = []
        for i in range(n):
            heapq.heappush(h, T(nums1[i], nums2[0], 0))

        res = []
        for i in range(k):
            if not h:
                break
            t = heapq.heappop(h)
            res.append([t.a, t.b])
            if t.i + 1 < m:
                heapq.heappush(h, T(t.a, nums2[t.i + 1], t.i + 1))
        return res
