"""

link: https://leetcode.com/problems/find-the-duplicate-number

problem: 数组长度 n+1 ，元素∈ [0,n]，其中有且仅有只有一个重复值，找出来，要求时间O(n^2)内，空间O(1)

solution: 快慢指针。由于元素始终在下标范围内，将题目转换成，nums[i] 指向 nums[nums[i]] 的图，求其环。
          就可以用快慢指针求环交点的做法处理了，时间O(n)，空间O(1)

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = nums[slow]
        t = nums[0]
        while t != slow:
            slow = nums[slow]
            t = nums[t]
        return t
