"""

link: https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self

problem: 求数组每个位置后有多少元素比该位数字小

solution: 桶排 + 树状数组。从后向前做桶排序，每个数字一个桶，每次将数字nums[i]排序后，利用树状数组计算 [1, nums[i]] 个桶中共有多少数字。

"""
class BinaryIndexTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def low_bit(self, x):
        return x & (-x)

    def add(self, k, v):
        while k < len(self.tree):
            self.tree[k] += v
            k += self.low_bit(k)

    def sum(self, k) -> int:
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= self.low_bit(k)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree, p = BinaryIndexTree(2 * 10 ** 4 + 1), 10 ** 4 + 1
        res = [_ for _ in nums]

        n = len(nums)
        for i in range(n - 1, -1, -1):
            tree.add(nums[i] + p, 1)
            res[i] = tree.sum(nums[i] + p - 1)
        return res
