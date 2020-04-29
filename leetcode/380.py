"""

link: https://leetcode.com/problems/insert-delete-getrandom-o1

problem: 实现随机集合，要求能 O(1) 的执行 insert / remove / getRandom 操作

solution: 在 insert 和 remove 时隐含了 get 的操作，O(1) 必须为 map，O(1) 的getRandom 则应通过数组的随机下标。使用 map 和 list 组合来实现
          此数据结构，list 存实际值，map 存位置，移除时交换待移除元素到 list 末尾以实现 O(1) 级别的删除元素。

"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.data.append(val)
        self.pos[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        self.data[self.pos[val]] = self.data[-1]
        self.pos[self.data[-1]] = self.pos[val]
        self.data.pop()
        del self.pos[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
