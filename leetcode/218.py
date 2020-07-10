"""

link: https://leetcode-cn.com/problems/the-skyline-problem

problem: 用数组代表建筑的 （左x轴坐标，右x轴坐标，y轴高度），求其轮廓线

solution: 平衡树。将左上和右上坐标取出排序，对左上入树，右上出树，记录过程的扫描高度，当高度发生差异时，即为轮廓线节点。
          python 没有现成的平衡树，用 dict 代替了 multiset 进行存取，用 c++ 写更优。

solution-fix: 线段树 + 离散化 + 懒加载。将建筑理解成 (l, r) 的线段染色为 h，重复染色以 h 更高为准，即为标准的区间染色问题，线段树基础操作。

"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        c, bound_list = collections.defaultdict(int), []
        for b in buildings:
            bound_list.append((b[0], b[2], True))
            bound_list.append((b[1], b[2], False))
        bound_list.sort()
        height = 0
        res = []
        for i, x in enumerate(bound_list):
            # 左上，入树
            if x[2]:
                c[x[1]] += 1
            # 右上，出树
            else:
                if c[x[1]] == 1:
                    c.pop(x[1])
                else:
                    c[x[1]] -= 1
            # 若与下一位，x轴重叠，以下一个坐标为准，因为排序顺序肯定下一个坐标更高，会覆盖此坐标
            if i < len(bound_list) - 1 and bound_list[i + 1][0] == x[0]:
                continue
            t = height
            height = 0 if len(c) == 0 else max(c)
            if t != height:
                res.append((x[0], height))
        return res
