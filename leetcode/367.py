"""

link: https://leetcode.com/problems/valid-perfect-square

problem: 不使用sqrt，检查是否完全平方数

solution: 二分查。

"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l + r) >> 1
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
