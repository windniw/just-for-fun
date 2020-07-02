"""

link: https://leetcode-cn.com/problems/two-sum-iii-data-structure-design

problem: 实现类，add 增加一个元素，find 查找 add 过的元素中是否有两个数相加等于 value

solution: map记录存取结果，注意 add 的值可能相等，不能用 set

"""
class TwoSum:

    def __init__(self):
        self.data = {}

    def add(self, number: int) -> None:
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1

    def find(self, value: int) -> bool:
        for x in self.data:
            if value - x in self.data and ((value - x == x and self.data[value - x] > 1) or (value - x != x)):
                return True
        return False
