"""

link: https://leetcode-cn.com/problems/meeting-rooms-ii

problem: 给定开区间数组代表会议的开始结束时间，问共需要几个会议室

solution: 排序。别一看会议室加区间就是排序贪心。。。本质上就是时序化的往管道中输入输出事件，求管道所需的最大空间。按时间扫一遍即可。

"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        event = [[x[0], 1] for x in intervals] + [[x[1], -1] for x in intervals]
        event.sort()
        res, cur = 0, 0
        for _, e in event:
            cur += e
            res = max(res, cur)
        return res
