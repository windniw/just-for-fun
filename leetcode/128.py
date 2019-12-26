"""

link: https://leetcode.com/problems/longest-consecutive-sequence

problem: 求数组的最长连续序列，要求时间O(n)

solution: 哈希。O(nlogn)的思路很容易想到，排个序再扫即可。O(n)利用了哈希集，先丢进集合，
          枚举每个元素 x, if x - 1 not in set, 则它为某个序列的首位，向后枚举每个数字直
          至其不在集合中为止

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        for x in s:
            if x - 1 not in s:
                t = x
                while t in s:
                    t += 1
                res = max(res, t - x)
        return res
