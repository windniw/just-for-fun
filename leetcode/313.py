"""

link: https://leetcode-cn.com/problems/super-ugly-number

problem: 定义丑数为质因数均在primes中的数，求第n个

solution: 丑数序列中的每个数，均可由之前某个数 *primes[x] 来得到，维护一个最小堆，每次将最小值t
          *primes[x] 重新放入堆中，并将 t 放入结果数组中，按顺序生成，时间复杂度 O(nk)

"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res, heap = [], []
        heapq.heappush(heap, 1)
        while len(res) < n:
            t = heapq.heappop(heap)
            if res and t == res[-1]:
                continue
            for x in primes:
                heapq.heappush(heap, t * x)
            res.append(t)
        return res[n - 1]