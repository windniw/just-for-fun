"""

link: https://leetcode.com/problems/triangle

problem: 三角列表，求从顶至下的最小路径，要求空间为O(n)

solution: DP。

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        res = [0 for _ in range(len(triangle))]
        for k in triangle:
            for j in reversed(range(len(k))):
                if j == len(k) - 1:
                    res[j] = res[j - 1]
                elif j != 0:
                    res[j] = min(res[j], res[j-1])
                res[j] += k[j]
        return min(res)