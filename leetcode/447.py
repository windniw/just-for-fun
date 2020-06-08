"""

link: https://leetcode.com/problems/number-of-boomerangs

problem: 给坐标数组，求三元组 (i, j, k) 满足 s(points[i], points(j)) == 
         s(points[j], points(k)) 的数量，其中 s 为两点的距离

solution: 暴力计几。

"""
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for k1 in points:
            t = collections.defaultdict(int)
            for k2 in points:
                x, y = k1[0] - k2[0], k1[1] - k2[1]
                t[x * x + y * y] += 1
            for x in t:
                res += t[x] * (t[x] - 1)
        return res
