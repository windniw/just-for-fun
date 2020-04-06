"""

link: https://leetcode.com/problems/top-k-frequent-elements

problem: 求数组频率前k的元素，要求时间复杂度优于 O(nlogn)

solution: 计算频率，遍历堆，抛出前k个元素，时间复杂度O(nlogk)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), count.get)
