"""

link: https://leetcode-cn.com/problems/target-sum

problem: 对数组每个元素补上正负号，问共有多少种方法使得数组元素和为 S，数组长度小于20，初始数组元素和不大于1000

solution: DP。直接搜时间复杂度O(2^20) 会 TLE，性能真烂。转变成有两个选择的 01 背包问题，扫一遍记录每轮的可能的结果有哪些。
          注意两个选择的结果会互相干扰，不能用 01 背包的倒序法遍历，需要另起临时数组存储每轮新的结果再换回来。

"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n, res, a = len(nums), 0, sum(nums)
        offset = a
        if not 0 <= offset + S <= a + offset:
            return 0
        cnt = [0 for _ in range(a * 2 + 10)]
        cnt[0 + offset] = 1
        for i in range(n):
            t = [0 for _ in range(a * 2 + 10)]
            for j in range(-a + offset, a + offset + 1):
                if cnt[j] != 0:
                    t[j + nums[i]] += cnt[j]
                    t[j - nums[i]] += cnt[j]
            cnt = t
        return cnt[S + offset]
