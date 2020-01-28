"""

link: https://leetcode-cn.com/problems/largest-number

problem: 计算数字拼凑最大值

solution: 排序。两两比对放置前后顺序的大小

"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def ncmp(a, b: int) -> int:
            aa, bb = str(a) + str(b), str(b) + str(a)
            return 1 if aa > bb else -1

        if len(nums) == 0:
            return "0"
        nums.sort(key=functools.cmp_to_key(ncmp), reverse=True)
        return "0" if nums[0] == 0 else "".join([str(x) for x in nums])
