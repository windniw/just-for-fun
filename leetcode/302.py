"""

link: https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels

problem: 给定 0, 1 矩阵，以及一个矩阵中为 1 的点坐标，求包含矩阵中所有的1的最小矩形面积

solution: 暴搜。忽略坐标，直接遍历所有节点，找到上下左右四个边界点，时间O(nm)。

"""

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        n, m = len(image), len(image[0])
        a, b, c, d = n, m, 0, 0
        for i in range(n):
            for j in range(m):
                if image[i][j] == '1':
                    a = min(a, i)
                    b = min(b, j)
                    c = max(c, i)
                    d = max(d, j)
        return (c + 1 - a) * (d + 1 - b)
