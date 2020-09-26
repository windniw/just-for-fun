"""

link: https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals

problem: 持续加入num，要求动态返回合并数字的区间，考虑区间稀疏与密集的情况

solution: 平衡树。稀疏时基本不存在区间合并，直接记录所有插入数字，查区间时拿出来遍历一遍合并。

solution-fix: 二分。密集时考虑快速合并能力，最终区间展开成一维数组一定是非严格递增情况。
              用一维数组保存所有区间，二分查找数字的插入点，插入位置为偶数时，num 位于已有区间内，否则在区间外，考虑左右区间的合并情况。
              这里用数组而不考虑平衡树存取修改，是因为平衡树不好处理单数字区间，左右边界相等的情况，还得拆成两棵树来记录。

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

# ---
class SummaryRanges:
    def __init__(self):
        self.data = []

    def addNum(self, val: int) -> None:
        p = bisect.bisect(self.data, val)
        if p & 1 == 1 or (p > 0 and self.data[p - 1] == val):
            return
        self.data.insert(p, val)
        self.data.insert(p, val)
        if p - 1 >= 0 and self.data[p - 1] + 1 == val:
            self.data.pop(p - 1)
            self.data.pop(p - 1)
            p = p - 2
        if p + 2 < len(self.data) and self.data[p + 2] == val + 1:
            self.data.pop(p + 1)
            self.data.pop(p + 1)

    def getIntervals(self) -> List[List[int]]:
        return zip(self.data[::2], self.data[1::2])
