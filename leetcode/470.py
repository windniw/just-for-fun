"""

link: https://leetcode-cn.com/problems/implement-rand10-using-rand7

problem: 用 rand7 实现 rand10

solution: 拒绝采样

"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        num = rand7() + (rand7() - 1) * 7
        while num > 40:
            num = rand7() + (rand7() - 1) * 7
        return num % 10 + 1