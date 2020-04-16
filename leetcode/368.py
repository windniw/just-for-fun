"""

link: https://leetcode.com/problems/largest-divisible-subset

problem: 求给定数组中的集合X，满足X的元素最多，且X中任意两个元素i,j 满足， i%j==0 || j%i==0

solution: DP。O(n^2)，排序后自小向大扫，dp[i] 定义为到扫描到i时，包括i的最大集合。

"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ll = [[] for _ in range(n)]
        for i in range(n):
            ll[i] = [nums[i]]
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and len(ll[j]) + 1 > len(ll[i]):
                    ll[i] = ll[j].copy()
                    ll[i].append(nums[i])
        res = []
        for x in ll:
            if len(res) < len(x):
                res = x
        return res
