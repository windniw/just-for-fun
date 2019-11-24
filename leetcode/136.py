"""

link: https://leetcode.com/problems/single-number

problem: 找到数组中只出现一次的数字，要求时间O(n)， 空间O(1)

solution: 时间O(n)可以用哈希表，空间O(1)可以用排序，两者均要利用异或特性 r^a^a=r

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
