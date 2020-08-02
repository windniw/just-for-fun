"""

link: https://leetcode-cn.com/problems/palindrome-permutation-ii

problem: 问给定字符串重新组合后能否回文，如果可以，输出所有可能的回文序列

solution: 枚举一半，生成另一半。
       
"""
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        m = collections.defaultdict(int)
        for x in s:
            m[x] += 1
        if sum([(m[x] & 1) for x in m]) > 1:
            return []
        t, sp, res = [], "", []
        for x in m:
            t += x * (m[x] // 2)
            if m[x] & 1:
                sp = x

        def f(n: int):
            if n >= len(t) - 1:
                k = ""
                for x in t:
                    k += x
                return res.append(k + sp + k[::-1])
            visit = set()
            for i in range(n, len(t)):
                if t[i] in visit:
                    continue
                visit.add(t[i])
                t[n], t[i] = t[i], t[n]
                f(n + 1)
                t[i], t[n] = t[n], t[i]
            return

        f(0)
        return res
