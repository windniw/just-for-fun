"""

link: https://leetcode-cn.com/problems/find-the-celebrity

problem: 求n个节点的图中入度为n-1，出度为0的点。

solution: 暴力。枚举查每个节点。时间O(n^2)。

solution-fix: 考虑入度为 n-1 ，出度为 0 的条件，即任意两个节点a,b间若 a -> b，则a肯定不是合法点，否则b肯定不是合法点。
              令初始可能的合法点为0，扫一遍，当不满足 x -> 0 时，替换可能的合法点，则扫完一轮时必然只存在一个可能的节点。
              检查该节点是否满足条件。时间O(n)

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

# ---
class Solution:
    def findCelebrity(self, n: int) -> int:
        j = 0
        for i in range(1, n):
            if knows(j, i):
                j = i
        for i in range(n):
            if i != j and (not knows(i, j) or knows(j, i)):
                return -1
        return j

