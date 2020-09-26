"""

link: https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals

problem: 持续加入num，要求动态返回合并数字的区间，考虑区间稀疏与密集的情况

solution: 平衡树。稀疏时基本不存在区间合并，直接记录所有插入数字，查区间时拿出来遍历一遍合并。

"""
class SummaryRanges:

    def __init__(self):
        self.data = set()

    def addNum(self, val: int) -> None:
        self.data.add(val)

    def getIntervals(self) -> List[List[int]]:
        if len(self.data) == 0:
            return []
        res, i, j = [], None, None
        for x in sorted(self.data):
            if i is None:
                i, j = x, x
            elif x == j + 1:
                j = x
            else:
                res.append([i, j])
                i, j = x, x
        res.append([i, j])
        return res


