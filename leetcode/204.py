"""

link: https://leetcode.com/problems/count-primes

problem: 求 [1,n) 的素数数

solution: 由低向高检查是否素数，且同时排除以检查点x为因数的更大值

solution-fix: 素数表筛素数法。其实根本不需要检查每个数字是否素数，只要由小向大以每个素数为因数向上填表即可。
              注意存在两个sqrt优化：
              1. 由小向大的第一层循环，只需要枚举到sqrt(n)即可，因为若 sqrt(n) < k <= n，且其为合数，则其一定存在某因数落在[2,sqrt(n)]
              2. 以枚举数x为因数的向上填表，起始位置为 x*x 而不是 x,因为小于 x*x 的合数，肯定存在某因数落在[2,sqrt(x)]，之前填过了

solution-fix-fix: 严格来说fix''并不是算法级别的优化，而是语言级别的。将以下语句
                  for t in range(x * x, n, x):
                    prime_array[t] = 0
                  转换为
                  prime_array[x * x:n:x] = [0] * (1 + (n - x * x - 1) // x)
                  之后，时间从 600ms 降到了 150ms


                 
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

# ---
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime_array = [1] * n
        prime_array[0], prime_array[1] = 0, 0
        for x in range(2, int(math.sqrt(n)) + 1):
            if prime_array[x]:
                for t in range(x * x, n, x):
                    prime_array[t] = 0
        return sum(prime_array)
