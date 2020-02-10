"""

link: https://leetcode.com/problems/kth-largest-element-in-an-array

problem: 求数组中的第k大值

solution: 排序后返回

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
