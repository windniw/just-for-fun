"""

link: https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements

problem: 每次对数组的 n-1 个数 +1，问至少多少次后，数组元素均相等

solution: 找规律。换位思考，【n-1】个数 +1，对最后的结果等同于【1】个数 -1，所有数均降到最低值即可

"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
