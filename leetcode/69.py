"""

link: https://leetcode.com/problems/sqrtx

problem: 求整数平方根

solution: 二分

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) >> 1
            if mid * mid >= x:
                r = mid
            else:
                l = mid + 1
        return l if l * l <= x else l - 1