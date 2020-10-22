"""

link: https://leetcode-cn.com/problems/non-overlapping-intervals

problem: 给若干区间，移除最少的区间后，所有区间不相交, 求移除数量

solution: 贪心。经典问题，按区间右侧排序后扫一遍。

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        c, res = float("-inf"), 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        for x in intervals:
            if x[0] < c:
                res += 1
            else:
                c = x[1]
        return res
