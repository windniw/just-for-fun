"""

link: https://leetcode-cn.com/problems/word-pattern-ii

problem: 判断模板串的字母与匹配串的子串能否唯一双向匹配

solution: 暴力搜索。按位递归模板串，用map记录每次的匹配值。

"""
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        n, m, cm, value_used = len(pattern), len(str), {}, set()

        def f(i: int, j: int) -> bool:
            if i >= n and j >= m:
                return True
            if i >= n or j >= m:
                return False
            if j + (n - i) > m:
                return False
            key = pattern[i]
            if key in cm:
                v = cm[key]
                if j + len(v) <= m and str[j:j + len(v)] == v:
                    return f(i + 1, j + len(v))
                else:
                    return False
            for jj in range(j + 1, m + 1):
                v = str[j:jj]
                if v in value_used:
                    continue
                cm[key] = v
                value_used.add(v)
                if f(i + 1, jj):
                    return True
                del (cm[key])
                value_used.remove(v)
            return False

        return f(0, 0)
