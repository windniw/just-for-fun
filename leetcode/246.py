"""

link: https://leetcode-cn.com/problems/strobogrammatic-number

problem: 问给定数字翻转 180° 后是否等于原值

solution: 扫一遍，注意 2，5 不在可翻转字符中

"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = ""
        for x in num:
            if x not in m:
                return False
            res += m[x]
        res = res[::-1]
        return res == num
