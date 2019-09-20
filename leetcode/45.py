"""

link: https://leetcode.com/problems/jump-game-ii

problem: 定义nums为，位于nums[k]，可跳到[k-nums[k],k+nums[k]]，问从0跳到n-1，至少需要几步

solution: 55题的复杂版本。贪心，每次取所有当前决策中，下一步可到达最远的点，注意，不是这一次决策可到达的最远点
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur, cnt = 0, 0
        while cur < len(nums) - 1:
            if cur + nums[cur] >= len(nums) - 1:
                return cnt + 1
            max_next = cur + 1
            for i in range(cur + 2, cur + nums[cur] + 1):
                if nums[i] + i >= nums[max_next] + max_next:
                    max_next = i
            cur = max_next
            cnt += 1
        return cnt
