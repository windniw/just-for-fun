"""

link: https://leetcode.cn/problems/find-the-key-of-the-numbers

problem: 三个数字，求每位的最小值拼成的数字

tag: easy

solution: 遍历

solution-fix: 用取模代替字符串转换

"""

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def to_str(num):
            s = str(num)
            if len(s) < 4:
                s = '0' * (4 - len(s)) + s
            return s
        s1, s2, s3 = to_str(num1), to_str(num2), to_str(num3)
        res = ''
        for i in range(4):
            res += min(s1[i], s2[i], s3[i])
        return int(res)

# ---
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        p, res = 1, 0
        for i in range(4):
            res += min(num1 % 10, num2 % 10, num3 % 10) * p
            num1 //= 10
            num2 //= 10
            num3 //= 10
            p *= 10
        return res