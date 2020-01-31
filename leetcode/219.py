"""

link: https://leetcode.com/problems/contains-duplicate-ii

problem: 判断是否存在(i,j)，满足nums[i] == nums[j] and abs(i-j) <= k

solution: 字典存某数字最近出现位置

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in m and i - m[x] <= k:
                return True
            m[x] = i
        return False
