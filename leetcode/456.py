"""

link: https://leetcode-cn.com/problems/132-pattern

problem: 问数组 nums 是否存在 nums[i] < nums[k] < nums[j] && i < j < k 的元组

solution: 单调栈。对每个nums[j]，通过 f[j] 记录 min(nums[:j+1]) 来维护 j 元素的最小 nums[i]；
          从右向左维护递减单调栈来找到 nums[k]。

"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        n, f = len(nums), [nums[0]]
        for i in range(1, n):
            f.append(min(f[i - 1], nums[i]))
        stack = []
        for i in range(n - 1, -1, -1):
            if f[i] == nums[i]:
                continue
            k = nums[i]
            while stack and k > stack[-1]:
                if f[i] < stack.pop() < k:
                    return True
            stack.append(k)
        return False
