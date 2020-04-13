"""

link: https://leetcode.com/problems/guess-number-higher-or-lower

problem: 猜数

solution: 二分

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            t = guess(mid)
            if t == 0:
                return mid
            elif t > 0:
                l = mid + 1
            else:
                r = mid - 1
        return l
