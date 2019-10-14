"""

link: https://leetcode.com/problems/combinations

problem: 求C(n,k)的值集合

solution: 递归遍历，为防止重复，规定必须递增搜索

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def c(keys: [int], m: int) -> List[List[int]]:
            if m == 1: return [[i] for i in keys]
            t = []
            for i in range(0, len(keys) + 1 - m):
                for sub_res in c(keys[i + 1:], m - 1):
                    t.append([keys[i]] + sub_res)
            return t

        return c(range(1, n + 1), k)