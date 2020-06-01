"""

link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

problem: 求数组 nums[i] ^ nums[j] 的最大值，0 <= i, j < len(nums)，要求时间O(n)

solution: 字典树。最简单的搞法当然是枚举i,j，在此基础上做压缩。每扫过一个数时将其入树，
          同时找到该数在树中的最大异或对象，显然由高位至低位贪心，尽可能走对每位取反的
          路径可得该值。

"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root, res = {}, 0
        L = len(bin(max(nums))) - 2
        for x in nums:
            k = 1 << L
            store, visit, res_cur = root, root, 0
            while k:
                t = 1 if k & x else 0
                k >>= 1
                if t not in store:
                    store[t] = {}
                store = store[t]
                if 1 - t in visit:
                    visit = visit[1 - t]
                    res_cur = (res_cur << 1) + 1
                else:
                    visit = visit[t]
                    res_cur = (res_cur << 1) + 0
            res = max(res, res_cur)
        return res
