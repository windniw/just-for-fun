"""

link: https://leetcode.com/problems/different-ways-to-add-parentheses

problem: 给运算式，返回任意运算优先级下所有可能的结果

solution: 分治搜索所有 a op b 的可能结果

"""
import functools

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        nums, fs = [], []
        n = 0
        for x in input:
            if str.isalnum(x):
                n = n * 10 + int(x)
            else:
                nums.append(n)
                fs.append(x)
                n = 0
        nums.append(n)

        @functools.lru_cache(maxsize=None)
        def f(i1: int, i2: int) -> List[int]:
            if i1 == i2:
                return [nums[i1]]
            res = []
            for x in range(i1, i2):
                l1, l2 = f(i1, x), f(x + 1, i2)
                for t1 in l1:
                    for t2 in l2:
                        if fs[x] == "+":
                            res.append(t1 + t2)
                        elif fs[x] == "-":
                            res.append(t1 - t2)
                        elif fs[x] == "*":
                            res.append(t1 * t2)
            return res

        return f(0, len(nums)-1)
