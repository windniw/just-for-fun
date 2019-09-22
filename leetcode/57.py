"""

link: https://leetcode.com/problems/insert-interval

problem: 给定区间数组与一个插入区间，尽可能合并相邻区间后返回有序数组

solution: 同56的思路，先塞进去然后该怎么处理怎么处理

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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
