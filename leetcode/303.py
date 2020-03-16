"""

link: https://leetcode.com/problems/range-sum-query-immutable

problem: 离线计算数组区间和

solution: 转存 sum[:i]

"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            self.s[i] = self.s[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.s[j + 1] - self.s[i]
    