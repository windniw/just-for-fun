"""

link: https://leetcode-cn.com/problems/construct-the-rectangle

problem: 给定 C，求 A, B 满足 A*B == C 且 A >= B 且 A，B尽可能接近

solution: 开方后找最近的因数

"""
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        t = math.floor(math.sqrt(area))
        for i in range(t, 0, -1):
            if area % i == 0:
                return [area // i, i]
