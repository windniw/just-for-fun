"""

link: https://leetcode-cn.com/problems/paint-house

problem: 给 n*3 的数组，每项选一个数字，相邻选中的列数不能一致

solution: DP

"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n0, n1, n2 = 0, 0, 0
        for x in costs:
            t0 = min(n1, n2) + x[0]
            t1 = min(n0, n2) + x[1]
            t2 = min(n0, n1) + x[2]
            n0, n1, n2 = t0, t1, t2
        return min(n0, n1, n2)
