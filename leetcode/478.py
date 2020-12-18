"""

link: https://leetcode-cn.com/problems/generate-random-point-in-a-circle

problem: 给定圆，产生圆内的均匀随机点

solution: 转换为极坐标，随机生成极径和极角，注意极径需要开平方根。

"""
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        l = self.r * math.sqrt(random.random())
        t = random.random() * math.pi * 2
        return [self.x + l * math.sin(t), self.y + l * math.cos(t)]
