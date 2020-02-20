"""

link: https://leetcode.com/problems/summary-ranges

problem: 合并数组的连续区间

solution: 按顺序扫一遍

"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        st, en, res = nums[0], nums[0], []
        for x in nums:
            if x == en + 1 or x == en:
                en = x
            else:
                res.append(str(st) + "->" + str(en)) if st != en else res.append(str(st))
                st, en = x, x
        res.append(str(st) + "->" + str(en)) if st != en else res.append(str(st))
        return res
