"""

link: https://leetcode-cn.com/problems/meeting-rooms

problem: 判断给定开区间是否相交

solution: 排序完扫一遍

"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
