"""

link: https://leetcode.com/problems/powx-n

problem: 快速幂

solution: 用 x**n = (1/x)**(-n) 处理下 n 为负数情况即可
另，其实直接return  x**n 也可以的，性能基本一致

"""

class Solution:
    def __pow(self, x: float, n: int):
        debug(x, n)
        if n == 1: return x
        t = self.__pow(x, n >> 1)
        return t * t if n % 2 == 0 else t * t * x

    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        return self.__pow(x, n) if n > 0 else self.__pow(1 / x, -n)
