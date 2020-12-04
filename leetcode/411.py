"""

link: https://leetcode-cn.com/problems/minimum-unique-word-abbreviation

problem: 给定长为 m 的 target 字符串，与长为 n 的字符串数组，求 target 的最短缩写，且该缩写不为数组中任一子串的缩写。log2(n) + m ≤ 20。

solution: 搜索。搜索上限为 n * 2^m == 2^(log_2(n)) * 2^m == 2^(log_2(n) + m) <= 2^20。
          枚举 target 的每个缩写（遍历 [0, 1 << m)，用 0 代表该位压缩，1代表不压缩）并检查是否是有其他字符串在未缩写位置上均与其相同。

"""
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        m, l = len(target), []
        for k in dictionary:
            if len(k) == m:
                l.append(k)
        if not l:
            return str(m)
        res = target

        def g_str(t: [int]):
            c, x = 0, ""
            for k in t:
                if c != k:
                    x += str(k - c)
                c = k + 1
                x += target[k]
            if c != m:
                x += str(m - c)
            return x

        for i in range(0, 1 << m):
            t = []
            for j in range(m):
                if i & (1 << j):
                    t.append(j)
            cnt = 0
            for k in l:
                match = True
                for j in t:
                    if k[j] != target[j]:
                        match = False
                        break
                cnt += 1 if match else 0
                if cnt > 1:
                    break
            if cnt < 1:
                cur_str = g_str(t)
                if len(cur_str) < len(res):
                    res = cur_str
        return res
