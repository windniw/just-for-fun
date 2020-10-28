"""

link: https://leetcode-cn.com/problems/assign-cookies

problem: 给数组 g, s，两两匹配使得 g[i] <= s[j]，问最多能匹配多少对

solution: 贪心。排序后归并。

"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        i, j, n, m, res = 0, 0, len(g), len(s), 0
        g.sort()
        s.sort()
        while i < n and j < m:
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
                res += 1
        return res
