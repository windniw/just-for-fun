"""

link: https://leetcode-cn.com/problems/find-permutation

problem: 有长度 n 由 [1, n] 组成的字符串 str，给定用 D,I 表达的其每相邻元素间的大小关系，求字典序最小的字符串 str

solution: 贪心。分成若干 D,I 段，由 1 向 n 生成，I 段正序，D 段逆序。

solution-fix: 贪心。可以默认正序，逆序部分翻转即可，不需要一位位生成。

"""
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return []
        s = "X" + s
        n = len(s)
        f, c, i = [0] * n, 1, 1
        if s[1] == 'I':
            f[0] = 1
            c = 2
        while i < n:
            p, t = i, s[i]
            while i < n and s[i] == t:
                i += 1
            if t == 'I':
                for j in range(p, i - 1):
                    f[j] = c
                    c += 1
            else:
                for j in range(i - 1, p - 2, -1):
                    f[j] = c
                    c += 1
        if s[-1] == 'I':
            f[n - 1] = n
        return f

# ---

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return []
        n = len(s)
        f, p1 = [i for i in range(1, n + 2)], -1

        def reverse_f(a, b):
            for i in range(a, (a + b) // 2 + 1):
                f[i], f[b + a - i] = f[b + a - i], f[i]

        for i in range(0, n):
            if s[i] == 'I':
                p1 = i
            elif s[i] == 'D' and (i + 1 >= n or s[i + 1] == 'I'):
                reverse_f(p1 + 1, i + 1)
        return f
