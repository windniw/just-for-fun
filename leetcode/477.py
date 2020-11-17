"""

link: https://leetcode-cn.com/problems/total-hamming-distance

problem: 求给定数组中，任意两数的二进制不同位数量，数组元素∈[0, 10^9]，数组长度∈[0, 10^4]

solution: 10^9 < 2^30。按位统计每位上的0，1数量，相乘即为任意两数在该位上的不同数量。

"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(30):
            cnt = 0
            for k in nums:
                cnt += 1 if k & (1 << i) else 0
            res += cnt * (len(nums) - cnt)
        return res  q
