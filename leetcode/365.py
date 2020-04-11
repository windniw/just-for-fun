"""

link: https://leetcode.com/problems/water-and-jug-problem

problem: 有容量为 x,y 的两个水桶，问能否得到总和为 z 的水

solution: 数论。将问题转变为能否有 a,b 满足 ax + by = z，根据裴蜀定理，有解当且仅当 z 为 x, y 的最大公约数的整倍数。

"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if not x or not y:
            return z == x or z == y
        return x + y >= z and z % math.gcd(x, y) == 0
