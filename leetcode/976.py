"""

link: https://leetcode-cn.com/problems/largest-perimeter-triangle/

problem: 从给定数组挑三条边组成三角形，求周长最长值

solution: 贪心。三角形的充要条件是 a+b>c，其中 a<=b<=c，显然三边尽量大且连续。排序后从大向小枚举c。

"""
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i] < A[i - 1] + A[i - 2]:
                return A[i - 2] + A[i - 1] + A[i]
        return 0
