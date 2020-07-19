"""

link: https://leetcode-cn.com/problems/strobogrammatic-number-ii

problem: 定义数字翻转 180° 等于原值的为翻转数，求长度为 n 的翻转数总量

solution: dfs。枚举左半部分，生成右半部分。

"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['0', '1', '8']

        def f(i: int) -> list:
            if i > n // 2 - 1 + (n & 1):
                return ['']
            num_list = ['1', '8']
            if i != 0:
                num_list.append('0')
            if not (n & 1 and i == n // 2):
                num_list.extend(['6', '9'])
            res, sub_res = [], f(i + 1)
            for num in num_list:
                for x in sub_res:
                    res.append(num + x)
            return res

        m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        t, res = f(0), []
        for x in t:
            xx = x
            for i in range(n // 2 - 1, -1, -1):
                xx += m[x[i]]
            res.append(xx)
        return res
