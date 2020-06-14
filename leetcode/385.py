"""

link: https://leetcode.com/problems/mini-parser

problem: 已有一个枚举类，支持 list 和 int 两种类型，实现一个语法解析器

solution: 栈

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
    def deserialize(self, s: str) -> NestedInteger:
        n_stack, i, n = [NestedInteger()], 0, len(s)

        def read_num() -> int:
            nonlocal i, n
            t, neg = 0, False
            while (i < n) and ('0' <= s[i] <= '9' or s[i] == '-'):
                if s[i] == '-':
                    neg = True
                else:
                    t = t * 10 + int(s[i])
                i += 1
            if neg:
                t *= -1
            return t

        while i < n:
            if s[i] == '[':
                i += 1
                new_item = NestedInteger()
                if n_stack:
                    n_stack[-1].add(new_item)
                n_stack.append(new_item)
                continue
            if s[i] == ']':
                i += 1
                n_stack.pop()
                continue
            if s[i] == ',':
                i += 1
                continue
            n_stack[-1].add(NestedInteger(read_num()))
        return n_stack[0].getList()[0]
