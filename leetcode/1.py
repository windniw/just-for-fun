"""

link: https://leetcode.cn/problems/two-sum

problem: 给数组与定值，有且仅有唯一解两数之和等于该定值，求两数各自坐标，时间复杂度小于 O(n^2)

solution: O(nlogn) 记录坐标，按值排序，左右指针遍历

solution-fix： O(n) 扫一遍，哈希记录已经出现的数字

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nn = s
        for i in range(len(nums)):
            nn.append([nums[i], i])
        nn.sort()
        i, j = 0, len(nums) - 1
        while i <= j:
            if nn[i][0] + nn[j][0] < target:
                i+=1
            elif nn[i][0] + nn[j][0] > target:
                j-=1
            else:
                return [nn[i][1], nn[j][1]]

# 同思路，但用 nums 的值排序 nums 的下标，节省建立二维数组的空间
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nn = sorted(range(len(nums)), key=lambda k: nums[k])
        i, j = 0, len(nums) - 1
        while i <= j:
            t = nums[nn[i]] + nums[nn[j]]
            if t < target:
                i += 1
            elif t > target:
                j -= 1
            else:
                return [nn[i], nn[j]]


# ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, k in enumerate(nums):
            if k in m:
                return [m[k], i]
            m[target - k] = i
