"""

link: https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i

problem: 求数组最短子串的长度，要求子串满足或运算结果大于等于 k

tag: easy,try,滑动窗口

solution: 暴搜

solution-fix: 或运算满足递增规律，可以通过滑动窗口优化

"""
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n, res = len(nums), float('inf')
        for i in range(n):
            x = nums[i]
            if x >= k:
                return 1
            for j in range(i+1, n):
                x |= nums[j]
                if x >= k:
                    res = min(res, j - i + 1)
        if res == float('inf'):
            return -1
        return res

# ---
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return -1 if not nums else 1
        n, max_bit_length = len(nums), 32
        bs = [0] * max_bit_length
        i, j, res = 0, 0, float('inf')
        t = 0
        while i < n and j <= n:
            if t >= k:
                for b in range(max_bit_length):
                    bs[b] -= nums[i] & (1 << b)
                res = min(res, j - i)
                i += 1
            else:
                if j < n:
                    for b in range(max_bit_length):
                        bs[b] += nums[j] & (1 << b)
                j += 1
            t = 0
            for b in range(max_bit_length):   
                if bs[b] > 0:
                    t |= 1 << b
        if res == float('inf'):
            return -1
        return res