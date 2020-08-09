"""

link: https://leetcode-cn.com/problems/find-the-celebrity

problem: 求n个节点的图中入度为n-1，出度为0的点。

solution: 暴力。枚举查每个节点。时间O(n^2)。

"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            famous = True
            for j in range(n):
                if j == i:
                    continue
                if not knows(j, i):
                    famous = False
                    break
            if famous:
                for j in range(n):
                    if j == i:
                        continue
                    if knows(i, j):
                        famous = False
                        break
            if famous:
                return i
        return -1
