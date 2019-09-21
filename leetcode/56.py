"""

link: https://leetcode.com/problems/merge-intervals

problem: 给定区间数组，尽可能合并相邻区间

solution: 排个序扫一遍即可

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort()
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for k in intervals:
            if k[0] > right:
                res.append([left, right])
                left, right = k[0], k[1]
            right = max(right, k[1])
        res.append([left, right])
        return res
