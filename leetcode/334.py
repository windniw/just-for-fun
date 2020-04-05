"""

link: https://leetcode.com/problems/increasing-triplet-subsequence

problem: 验证给定的序列中是否存在长度为3的严格递增序列

solution: 双指针扫，记录每个点从左向右的最小值，从右向左的最大值，再比较一次。时间O(n)，空间O(n)

solution-fix: 扫一遍。很trick的一种做法，用 first, second 两个值来记录扫描过程的中间值
              若 x > second，则出现了递增三元组，返回True
              若 first < x <= second，则出现了更小的second，直接替换 second=x
              若 x < first，直接 first = x；注意此时出现了 first > second 的情况，但并不影响最后的结果。
              是否满足条件是依赖 second 的，second 值存在时代表在扫描过程中，确实存在比second小的值在左边，其值具体为多少已经不重要了
              时间 O(n)，空间 O(1)
"""

class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        if n < 3:
            return False
        left, right = [_ for _ in range(n)], [_ for _ in range(n)]
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = min(left[i - 1], nums[i])
        right[-1] = nums[-1]
        for i in reversed(range(0, n - 1)):
            right[i] = max(right[i + 1], nums[i])
        for i in range(1, n - 1):
            if left[i] < nums[i] < right[i]:
                return True
        return False

# ---
class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        if n < 3:
            return False
        first, second = float("inf"), float("inf")
        for i in range(n):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] > second:
                return True
            else:
                second = nums[i]
        return False

