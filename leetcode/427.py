"""

link: https://leetcode.com/problems/construct-quad-tree

problem: 矩阵生成四叉树

solution: 递归分治

"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def f(x: int, y: int, l: int) -> Node:
            if l == 1:
                return Node(grid[x][y], True, None, None, None, None)
            a, b, c, d = f(x, y, l // 2), f(x, y + l // 2, l // 2), f(x + l // 2, y, l // 2), f(x + l // 2, y + l // 2,
                                                                                                l // 2)
            if a.val == b.val == c.val == d.val == 1:
                return Node(1, True, None, None, None, None)
            if a.val == b.val == c.val == d.val == 0:
                return Node(0, True, None, None, None, None)
            return Node(2, False, a, b, c, d)

        return f(0, 0, len(grid))
