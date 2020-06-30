"""

link: https://leetcode-cn.com/problems/missing-ranges

problem: 升序数组，元素范围∈[lower, upper]，返回缺失区间

solution: 模拟。扫一遍记录该位的期望值。

"""
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res, cur = [], lower
        for x in nums:
            if x > cur:
                res.append((cur, x - 1))
            cur = x + 1
        if upper > cur - 1:
            res.append((cur, upper))
        return [str(p[0]) if p[0] == p[1] else str(p[0]) + "->" + str(p[1]) for p in res]