"""

link: https://leetcode-cn.com/problems/next-greater-element-ii

problem: 求循环数组中每个数的下一个更大值，不存在时返回 -1

solution: 单调栈。遍历两次维护一个非严格递减的单调栈即可。

"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [_ for _ in nums]

        for i, v in enumerate(nums):
            while stack and stack[-1][1] < v:
                res[stack[-1][0]] = v
                stack.pop()
            stack.append((i, v))

        for i, v in enumerate(nums):
            if not stack:
                break
            while stack and stack[-1][1] < v:
                res[stack[-1][0]] = v
                stack.pop()

        for i, _ in stack:
            res[i] = -1

        return res
