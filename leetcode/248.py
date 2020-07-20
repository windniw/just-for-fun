"""

link: https://leetcode-cn.com/problems/strobogrammatic-number-iii

problem: 定义数字翻转 180° 等于原值的为翻转数，求区间 [low, high] 内的翻转数总量

solution: 搜索。对 len(low) < len(k) < len(high) 的直接数学法算出数量；枚举 len(k) = len(low) and k <= low 的数量 与
          len(k) = len(high) and k <= high 的数量，cal(len(low)) - less_in_n(low) + calc(len(high)) 即为解。当low本身
          也为翻转数时需加1。

"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        if int(low) > int(high):
            return 0
        n, m = len(low), len(high)
        map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        def cal(x: int):
            if x == 0:
                return 0
            if x == 1:
                return 3
            return (4 * 5 ** max((x // 2 - 1), 0) * 3) if x & 1 else 4 * 5 ** (x // 2 - 1)

        def less_in_n(x: str):
            n = len(x)

            def f(i: int) -> list:
                if i > n // 2 - 1 + (n & 1):
                    return ['']
                num_list = ['1', '8']
                if i != 0:
                    num_list.append('0')
                if not (n & 1 and i == n // 2):
                    num_list.extend(['6', '9'])
                num_list.sort()
                res, sub_res = [], f(i + 1)
                for num in num_list:
                    for k in sub_res:
                        res.append(num + k)
                return res

            t, res = f(0), 0
            if n == 1:
                t.append('0')
            for k in t:
                kk = k
                for i in range(n // 2 - 1, -1, -1):
                    kk += map[k[i]]
                if kk <= x:
                    res += 1
            return res

        res = 0
        if n != m:
            for x in range(n + 1, m):
                res += cal(x)
            res += cal(n) - less_in_n(low) + less_in_n(high)
        else:
            res = less_in_n(high) - less_in_n(low)

        def is_legal_low() -> bool:
            for i in range(n // 2):
                if not (low[i] in map and map[low[i]] == low[n - i - 1]):
                    return False
            return True

        if is_legal_low():
            res += 1

        return res
