"""

link: https://leetcode.com/problems/rotate-image/

problem: 原地90度反转一个n*n矩阵

solution: 坐标轴变换，按序交换 [x,y] -> [y,n-x] -> [n-x,n-y] -> [n-y,x] -> [x,y]

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for x in range((n + 1) // 2):
            for y in range(n // 2):
                matrix[x][y], matrix[y][n - 1 - x], matrix[n - 1 - x][n - 1 - y], matrix[n - 1 - y][x] = \
                    matrix[n - 1 - y][x], matrix[x][y], matrix[y][n - 1 - x], matrix[n - 1 - x][n - 1 - y]
        return
