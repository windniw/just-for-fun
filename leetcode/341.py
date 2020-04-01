"""

link: https://leetcode.com/problems/flatten-nested-list-iterator

problem: 完成迭代器

solution: 离线做法，强行转list

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        def to_list(x: NestedInteger):
            if x.isInteger():
                return [x.getInteger()]
            else:
                res = []
                for k in x.getList():
                    res.extend(to_list(k))
                return res

        self.data = []
        for x in nestedList:
            self.data.extend(to_list(x))
        self.k = -1
        
    def next(self) -> int:
        self.k += 1
        return self.data[self.k]
        
    def hasNext(self) -> bool:
        return len(self.data) != self.k + 1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())