"""

link: https://leetcode.com/problems/count-primes

problem: 求 [1,n) 的素数数

solution: 由低向高检查是否素数，且同时排除以检查点x为因数的更大值

"""
class Solution:
    def is_prime(self, x: int) -> bool:
        k, prim, up = 2, True, math.sqrt(x)
        while k <= up:
            if x % k == 0:
                prim = False
                break
            k += 1
        return prim

    def countPrimes(self, n: int) -> int:
        prime_array = [True] * (n + 1)
        for x in range(2, int(math.sqrt(n)) + 1):
            if not prime_array[x]:
                continue
            prime_array[x] = self.is_prime(x)
            t = 2
            while t * x < n:
                prime_array[t * x] = False
                t += 1
        cnt = 0
        for i in range(2, n):
            if prime_array[i]:
                cnt += 1
        return cnt
