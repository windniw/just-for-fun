"""

link: https://leetcode-cn.com/problems/flatten-2d-vector

problem: 实现一个迭代器，展开二维数组。

solution: 记录遍历中的下标，注意在初始化时可能首元素为空数组，需要做预初始化

"""

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.data = v
        i, j = 0, 0
        while i < len(self.data):
            if j >= len(self.data[i]):
                i += 1
                j = 0
            else:
                break
        self.i, self.j = i, j

    def next(self) -> int:
        i, j = self.i, self.j
        t = self.data[i][j]
        j += 1
        while i < len(self.data):
            if j >= len(self.data[i]):
                i += 1
                j = 0
            else:
                break
        self.i, self.j = i, j
        return t

    def hasNext(self) -> bool:
        return self.i < len(self.data)



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()