"""

link: https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed

problem: 实现随机集合，要求能 O(1) 的执行 insert / remove / getRandom 操作，允许重复元素

solution: 在 insert 和 remove 时隐含了 get 的操作，O(1) 必须为 map，O(1) 的 getRandom 则应通过数组的随机下标。使用 list + map + set 组合来实现
          此数据结构，set 存实际值，map 存位置，移除时交换待移除元素到 list 末尾以实现 O(1) 级别的删除元素。

"""

class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        self.data.append(val)
        if val in self.pos:
            self.pos[val].add(len(self.data) - 1)
            return False
        else:
            self.pos[val] = {len(self.data) - 1}
            return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        p = self.pos[val].pop()
        if not self.pos[val]:
            del (self.pos[val])
        if p + 1 != len(self.data):
            self.data[p], self.data[-1] = self.data[-1], self.data[p]
            self.pos[self.data[p]].remove(len(self.data) - 1)
            self.pos[self.data[p]].add(p)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)