"""

link: https://leetcode-cn.com/problems/russian-doll-envelopes

problem: 给二元组数组，定义当且仅当 x[0] < y[0] and x[1] < y[1] 时 x < y，求该数组任意组合后的最长上升子序列

solution: 本质上还是 LIS 算法，先对 envelopes 按 (x[0], -x[1]) 排序，即保证首位升序，当首位相同时，第二位降序排列，然后对第二位数组求 LIS。
          通过这么构造数组，排序后对任意 i < j，有
          若 e[i][0] == e[j][0], e[i][1] >= e[j][1]，i -> j 不可能在求 LIS 时被计算
          若 e[i][0] < e[j][0]，i -> j 能否被计入序列取决于 e[i][1] < e[j][1]，符合要求
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or len(envelopes) == 0:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [x[1] for x in envelopes]
        tail = [nums[0]]
        for i in range(1, n):
            p = bisect.bisect_left(tail, nums[i])
            if p == len(tail):
                tail.append(nums[i])
            else:
                tail[p] = nums[i]
        return len(tail)
