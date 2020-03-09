"""

link: https://leetcode.com/problems/peeking-iterator

problem: 给迭代器加个修饰类，实现peek方法

solution: 加一个元素做缓存

"""
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.data = iterator
        self.x = iterator.next()

    def peek(self):
        return self.x

    def next(self):
        t = self.x
        self.x = self.data.next() if self.data.hasNext() else None
        return t

    def hasNext(self):
        return self.x is not None

        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].