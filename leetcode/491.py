"""

link: https://leetcode-cn.com/problems/increasing-subsequences

problem: 输出nums的所有非严格递增子序列

solution: 预处理每个节点的下一跳，dfs

"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        jump = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] >= nums[i]:
                    jump[i].append(j)
        res = set()

        def dfs(k: int, l: [int]):
            for i in jump[k]:
                res.add(tuple(l + [nums[i]]))
                dfs(i, l + [nums[i]])

        for i in range(n):
            dfs(i, [nums[i]])
        return list(res)
