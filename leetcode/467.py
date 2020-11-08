"""

link: https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string

problem: 给字符串p，问循环字符串 a..za..za..z... 中共有 p 的多少个子串

solution: DP。显然若 p[i] 与 p[i+1] 不连续没有意义，可以分割开考虑；用 m[p[i]] 记录以 p[i] 开头的
          最长连续子串长度来处理多个连续块间的重复关系。

"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        m, n = collections.defaultdict(int), len(p)
        i, j = 0, 1
        while i < n:
            if j < n and ((ord(p[j]) - ord(p[j - 1]) == 1) or (p[j] == 'a' and p[j - 1] == 'z')):
                j += 1
            else:
                for k in range(i, j):
                    m[p[k]] = max(m[p[k]], j - k)
                i = j
                j += 1
        return sum(m.values())
