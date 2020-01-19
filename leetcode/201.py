"""

link: https://leetcode.com/problems/bitwise-and-of-numbers-range

problem: 求 [m,n] 区间的与

solution: 按位检查，若该位进1是否还在区间内

"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k, res = 0, 0
        while (1 << k) <= m:
            if m & (1 << k) == 0:
                k += 1
                continue
            t = (m & (m >> k << k)) + (1 << k)
            if t > n:
                res += 1 << k
            k += 1
        return res
