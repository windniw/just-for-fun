"""

link: https://leetcode.cn/problems/3sum/

problem: 求数组内，三个数相加等于0的所有可能，返回值列表

solution: O(n^2logn) 遍历指定中值，退化成 two sum 问题 

solution-fix: O(n^2) 遍历中值换成遍历首值，可以有效减少 two sum 时的搜索范围，再加上跳过相同数字的优化去掉 set 的开销

"""

def twoSum(nums: List[int], aim: int) -> List[List[int]]:
    i, j = 0, len(nums) - 1
    output = []
    while i < aim < j:
        if nums[i] + nums[j] == -nums[aim]:
            output.append((nums[i], nums[aim], nums[j]))
            i += 1
        elif nums[i] + nums[j] < -nums[aim]:
            i += 1
        else:
            j -=1
    return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        output = set()
        for i in range(1, len(nums)-1):
            for x in twoSum(nums, i):
                output.add(x)
        return [list(x) for x in output]

#---
def twoSum(nums: List[int], aim, l, r: int) -> List[List[int]]:
    i, j = l, r
    output = []
    while i < j:
        x = nums[i] + nums[j] + nums[aim]
        if x == 0:
            output.append([nums[aim], nums[i], nums[j]])
            i += 1
            j -= 1
            while i < j and nums[i] == nums[i-1]:
                i += 1
            while i < j and nums[j] == nums[j+1]:
                j -= 1
        elif x < 0:
            i += 1
        else:
            j -= 1
    return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        output = []
        for i in range(0, len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            output.extend(twoSum(nums, i, i+1, len(nums)-1))
        return output