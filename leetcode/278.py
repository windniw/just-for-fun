"""

link: https://leetcode.com/problems/first-bad-version

problem: 求序列中第一个异常值，异常值之后的值均也异常

solution: 二分

"""
class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            mid = (l + r) >> 1
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
