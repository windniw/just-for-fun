"""

link: https://leetcode.com/problems/super-pow

problem: 求 a ** b % 1337，b 为数组形式的大整数

solution: 快速幂，以 10 为底数，b以数组形式存储，以10为底不需要做除法，用2为底就会超时。

"""
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337
        if a == 0 or a == 1:
            return a
        a_list = [a ** i % 1337 for i in range(10)]
        res = 1
        for k in b:
            t = a_list[k]
            res = res ** 10 * t % 1337
            res %= 1337
        return res
