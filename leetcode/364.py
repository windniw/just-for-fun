"""

link: https://leetcode-cn.com/problems/nested-list-weight-sum-ii

problem: 嵌套序列求反向加权和

solution: 两边dfs。先求高度再计算。

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        def depth(k: NestedInteger) -> int:
            if k.isInteger():
                return 1
            t = 1
            for x in k.getList():
                t = max(t, depth(x))
            return t + 1
        d = 1
        for x in nestedList:
            d = max(d, depth(x))

        def f(k: NestedInteger, w: int) -> int:
            if k.isInteger():
                return k.getInteger() * w
            t = 0
            for x in k.getList():
                t += f(x, w-1)
            return t
        
        res = 0
        for x in nestedList:
            res += f(x, d)
        return res

