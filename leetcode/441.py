"""

link: https://leetcode.com/problems/arranging-coins

problem: 用n个硬币叠金字塔，求层数

solution: 二分

"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 65536
        while l < r:
            mid = (l + r) >> 1
            if mid * (mid + 1) // 2 <= n:
                l = mid + 1
            else:
                r = mid
        return l - 1
