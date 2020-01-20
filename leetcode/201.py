"""

link: https://leetcode.com/problems/bitwise-and-of-numbers-range

problem: 求 [m,n] 区间的与

solution: 自低位向高位看m，按位检查，若该位进1是否还在区间内

solution-fix: 自高位向低位看n，找最高位使m,n不同的1，显然再往下的每一位要么经历过进位，要么均为0，则其与
              肯定为 0; 问题转变为如何找到最高的不同的位，由低向高移除n的每个最低的1位即可

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

"---
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= n - 1
        return n