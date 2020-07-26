"""

link: https://leetcode-cn.com/problems/factor-combinations

problem: 分解因数，输出所有组合

solution: dfs。引入分解的起始因数大小做去重。踩了一个 lru_cache 的坑，返回 list 时对结果做 append 会影响cache的值，导致cache混乱。

"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def f(k: int, st: int):
            res = []
            for i in range(st, int(math.sqrt(k)) + 1):
                if k % i == 0:
                    t = f(k // i, i)
                    t.append([k // i])
                    res.extend([[i] + x for x in t])
            return res

        return f(n, 2)
