"""

link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

problem: 从有序数组找到两个数相加等于目标值，保证与且只有唯一解

solution: 左右指针遍历

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]