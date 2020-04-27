"""

link: https://leetcode.com/problems/is-subsequence

problem: 问 s 是否为 t 的子序列

solution: 贪心。对 s 的每位取其在 t 的最前值。

solution-fix: 问当t固定，而s有上亿个时应如何处理。预处理 t，记录每位的下一个可能字母位置，缩短检查t时的消耗。

"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in s:
            while i < len(t) and t[i] != x:
                i += 1
            if i == len(t):
                return False
            i += 1
        return True

# ---
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        next = [[-1] * 26 for _ in range(n + 1)]
        for i in range(26):
            k = -1
            for j in range(n, -1, -1):
                next[j][i] = k
                if j and t[j - 1] == chr(ord('a') + i):
                    k = j
        k = 0
        for c in s:
            if next[k][ord(c) - ord('a')] == -1:
                return False
            k = next[k][ord(c) - ord('a')]

        return True
