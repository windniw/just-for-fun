"""

link: https://leetcode-cn.com/problems/max-consecutive-ones-ii

problem: 给定数组，问其中最多间隔1个0的连续的1的长度

solution: 将连续的1分成两段来考虑，记录上一段1的数量，扫一遍

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        p1, p2, res = 0, 0, 0
        for k in nums:
            if k == 1:
                p2 += 1
            else:
                p1 = p2
                p2 = 0
            res = max(res, p1 + p2 + 1)
        return min(len(nums), res)
