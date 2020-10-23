"""

link: https://leetcode-cn.com/problems/find-right-interval

problem: 给区间集合，求检查其中每个区间存在的最近不相交右区间的下标

solution: 二分。按区间左侧排序，二分查找。

"""
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res, l = [], [(x[0], i) for i, x in enumerate(intervals)]
        l.sort()
        for x in intervals:
            i = bisect.bisect_left(l, (x[1], 0))
            res.append(-1 if i == len(l) else l[i][1])
        return res
