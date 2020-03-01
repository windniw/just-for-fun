"""

link: https://leetcode.com/problems/ugly-number

problem: 定义只有 2，3，5 的因数的自然数为丑数，求第n个丑数，n小于1690

solution: 丑数序列中的每个数，均可由之前某个数 *2/3/5 来得到，维护一个最小堆，每次将最小值t
          *2/3/5重新放入堆中，并将 t 放入结果数组中，按顺序生成。

solution-fix: 仍然是每次用最小值生成下一个丑数的原则。维护三个指针，i2,i3,i5 指向结果数组，每次取
              min(nums[i2]*2, nums[i3]*3, nums[i5]*5)为下一个丑数，并增加对应指针。注意可能存在
              重复，如 6 = 2*3 = 3*2，若有相同的最小值，各指针均应自增。

"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, heap = [], []
        heapq.heappush(heap, 1)
        while len(res) < n:
            t = heapq.heappop(heap)
            if res and t == res[-1]:
                continue
            heapq.heappush(heap, t * 2)
            heapq.heappush(heap, t * 3)
            heapq.heappush(heap, t * 5)
            res.append(t)
        return res[n - 1]

# ---
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        res = [1]
        for _ in range(n):
            t = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            res.append(t)
            if t == res[i2] * 2:
                i2 += 1
            if t == res[i3] * 3:
                i3 += 1
            if t == res[i5] * 5:
                i5 += 1
        return res[n - 1]