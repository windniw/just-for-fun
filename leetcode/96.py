"""

link: https://leetcode.com/problems/unique-binary-search-trees

problem: 求[1,n]合法的二叉排序树数量

solution: DP

"""

class Solution:
    def numTrees(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]
        f[0] = 1

        for i in range(n + 1):
            for j in range(0, i):
                f[i] += f[j] * f[i - 1 - j]

        return f[n]