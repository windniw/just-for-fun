"""

link: https://leetcode-cn.com/problems/teemo-attacking

problem: 以 timeSeries 数组的每个点为左端点标记一段长为 duration 的区间，问区间总长

solution: 排序扫一遍，排除重复区间部分。

"""
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.sort()
        res, n = 0, len(timeSeries)
        for i, v in enumerate(timeSeries):
            if i != n - 1 and timeSeries[i + 1] < v + duration:
                res += timeSeries[i + 1] - v
            else:
                res += duration
        return res
