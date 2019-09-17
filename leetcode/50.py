"""

link: https://leetcode.com/problems/powx-n

problem: 快速幂

solution: 用 x**n = (1/x)**(-n) 处理下 n 为负数情况即可
另，其实直接return  x**n 也可以的，性能基本一致

solution-fix: x**n = x**(2**i1 + 2**i2) = x**2**i1 * x**2**i2
所以只要知道 x**2**i(i∈[1,logn]) 的值，当n的二进制的i位是1时，把值往上乘即可，省了递归步骤 

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

# ---
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res, t = 1, x
        while n != 0:
            if n & 1: res *= t
            t *= t
            n >>= 1
        return res
