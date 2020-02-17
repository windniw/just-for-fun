"""

link: https://leetcode.com/problems/combination-sum-iii/submissions

problem: 用[1,9]中的k个数字组成n，求多少种组合，要求数字不能相同

solution: 递归搜

"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def f(k: int, n: int, i: int) -> List[List[int]]:
            if i > 9 or n < 1:
                return []
            if n > (10 - k + 9) * k // 2 or n < (i + i - 1 + k) * k // 2:
                return []
            if k == 1:
                return [[n]]
            res = []
            for ii in range(i, 10):
                t = f(k - 1, n - ii, ii + 1)
                if t:
                    for x in t:
                        xx = [ii]
                        xx.extend(x)
                        res.append(xx)
            return res

        return f(k, n, 1)