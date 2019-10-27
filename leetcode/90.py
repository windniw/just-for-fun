"""

link: https://leetcode.com/problems/subsets-ii

problem: 给可能重复序列nums，求所有子集

solution: 类78。先排序，求全子集，丢集合过滤再转数组出来

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in nums:
            res += [[i] + j for j in res]
        return [list(i) for i in set([tuple(i) for i in res])]