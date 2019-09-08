"""

link: https://leetcode.com/problems/multiply-strings

problem: 大数乘法

solution: 模拟就完事了

solution-fix: 快速傅里叶变换可以优化到 O(NlgN) 的级别，不过这玩意已经忘光了，就不写了

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                t = (ord(num1[i]) - 48) * (ord(num2[j]) - 48) + res[i + j + 1]
                res[i + j + 1] = t % 10
                res[i + j] += t // 10
        return ''.join([chr(i + 48) for i in res]).lstrip('0')
