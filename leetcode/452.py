"""

link: https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons

problem: 给若干区间，问最少需要几个点，能使得任意区间均包含某一个点

solution: 贪心。按左端升序排列，贪心维护点的分布区间；当下一个区间与点分布区间不相交时，选择下一个区间为新的可选分布区间。

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        cnt, l, r = 1, points[0][0], points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= r:
                l = max(l, points[i][0])
                r = min(r, points[i][1])
            else:
                cnt += 1
                l, r = points[i][0], points[i][1]
        return cnt
