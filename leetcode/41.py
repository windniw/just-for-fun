"""

link: https://leetcode.com/problems/first-missing-positive

problem: 求nums中最小的未出现正整数，要求时间复杂度O(n), 空间复杂度O(1)

solution: 桶排序，忽略掉 <= 0 || >= len(nums) 的值，原地交换解决空间复杂度的问题即可

solution-fix: [官方题解] 本质还是桶排，不过处理空间复杂度的思路不同，已知答案肯定落在 [1, len(nums)]，
              先扫一轮把所有 <=0 的替换成 len(nums)+1，再将所有数字取反
              这样所有的数字均为负数了，原数组腾出一个正负位，用来存储是否信息，即将原数组扩展出bitmap的位置
              后面跟桶排思想一致直接做就行了
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

# ---

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)

        for i in range(size):
            nums[i] = -(size + 1) if nums[i] <= 0 or nums[i] > size else -nums[i]

        for k in nums:
            if 0 < abs(k) <= size:
                nums[abs(k)-1] = abs(nums[abs(k)-1])

        for i in range(size):
            if nums[i] <= 0:
                return i+1
        return size + 1
