"""

link: https://leetcode.com/problems/spiral-matrix-ii

problem: 给定n，按逆时针顺序生成[1,n*n]的矩阵

solution: 按照(k,k) k∈[0,(n+1)//2)的顺序由外向里模拟即可

"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x = 0

        def next_number():
            nonlocal x
            x += 1
            return x

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range((n+1) // 2):
            for j in range(i, n - i - 1 + 1):
                matrix[i][j] = next_number()
            for j in range(i + 1, n - i - 1 + 1):
                matrix[j][n - i - 1] = next_number()
            for j in range(n - i - 1 - 1, i - 1, -1):
                matrix[n - i - 1][j] = next_number()
            for j in range(n - i - 1 - 1, i, -1):
                matrix[j][i] = next_number()
        return matrix
