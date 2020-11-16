"""

link: https://leetcode-cn.com/problems/heaters

problem: 给定数轴上若干A类型的点，再给B类型的点，问以所有B为圆心画圆，最小半径是多少可以覆盖所有的A

solution: 二分。所有A点由其最近的B负责覆盖，结果为此集合中的最大值。

"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            p = bisect.bisect_left(heaters, house)
            a, b = float("inf"), float("inf")
            if p != len(heaters):
                a = max(heaters[p] - house, res)
            if p != 0:
                b = max(house - heaters[p - 1], res)
            res = max(res, min(a, b))
        return res
