"""

link: https://leetcode-cn.com/problems/maximum-gap

problem: 非负整数序列，求排序后相邻元素的最大差，要求时间O(n)，空间O(n)

solution: 桶排。

"""
class Solution:
    class Bucket:
        def __init__(self):
            self.min_num = float("inf")
            self.max_num = float("-inf")
            self.has_num = False

        def update(self, x: int):
            self.min_num = min(self.min_num, x)
            self.max_num = max(self.max_num, x)
            self.has_num = True

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_num, min_num = max(nums), min(nums)
        # 桶大小，注意这个 -1
        # 在桶的元素极度稀疏时，每个桶中都会有一个元素，即最大差一定存在桶之间
        # 若某个桶存在了两个元素，则必然有空桶，则最大差也一定在桶之间，因为桶内元素的差不可能大于一个空桶的间隔
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        # 桶数量，+1 包括了 min_num 所在的桶
        bucket_num = (max_num - min_num) // bucket_size + 1
        # 初始化桶
        buckets = [self.Bucket() for _ in range(bucket_num)]
        for x in nums:
            i = (x - min_num) // bucket_size
            buckets[i].update(x)
        # 最大间隔只可能存在相邻的有元素的桶里，遍历桶找最大值
        # 最极限情况下，所有元素完全重合，此时最大差 0 出现在桶内，初始化 res 为 0
        res, pre_bucket_max_num = 0, min_num
        for b in buckets:
            if not b.has_num:
                continue
            res = max(res, b.min_num - pre_bucket_max_num)
            pre_bucket_max_num = b.max_num
        return res
