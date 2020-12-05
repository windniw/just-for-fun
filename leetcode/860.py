"""

link: https://leetcode-cn.com/problems/lemonade-change

problem: 按序给钞票 5, 10, 20，每次定额消耗 5，并用已有钞票找零，问是否满足

solution: 贪心。先找回面额大的。

"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a, b, c = 0, 0, 0
        m = {20: [(-1, -1, 1), (-3, 0, 1)], 10: [(-1, 1, 0)], 5: [(1, 0, 0)]}
        for k in bills:
            done = False
            for x in m[k]:
                if a >= -x[0] and b >= -x[1]:
                    a += x[0]
                    b += x[1]
                    c += x[2]
                    done = True
                    break
            if not done:
                return False
        return True
