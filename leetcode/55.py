"""

link: https://leetcode.com/problems/jump-game

problem: 定义nums为，位于nums[k]，可跳到[k-nums[k],k+nums[k]]，问第n-1是否可达

solution: 45题的简化版，更新最远距离即可

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bound = 0
        for i in range(0, len(nums)):
            if bound < i:
                return False
            bound = max(bound, i + nums[i])
        return True