"""

link: https://leetcode.com/problems/happy-number

problem: 定义函数f为一个数字n的每位数字平方和，给数字问能否通过有限次f得到1

solution: 模拟

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            m = n
            n = 0
            while m:
                n += (m % 10) * (m % 10)
                m = m // 10
            if n in s:
                return False
            if n == 1:
                return True
            s.add(n)
