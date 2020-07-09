"""

link: https://leetcode-cn.com/problems/shortest-palindrome

problem: 给字符串s，在s前补字符使其成为回文串，求补完后的最短回文串

solution: KMP。显然问题可以转变为，求最长的 s[:k] 回文子串，剩余的 s[k:] 补在前面既是所求解。问题转换为如何快速判断 s[:1], s[:2]...
          是否为回文子串，将 s + '#' + s[::-1] 拼起来记为 ss，对其求 kmp 的 next 数组，根据 kmp 定义可知有
          s[:next[-1]] == ss[n-next[-1]:]
          又因为 ss 后半部分为 s 的翻转，有
          ss[n-next[-1]:] == s[:next[-1]:-1]
          则 s[:next[-1]] == s[:next[-1]:-1]，即回文定义，所以最长的子串即为next数组的最末值。

"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p = s + '#' + s[::-1]
        n, m = len(p), len(s)
        next_list, i, j = [0 for _ in range(n + 1)], 0, -1
        next_list[0] = -1
        while i < len(p):
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                next_list[i] = j
            else:
                j = next_list[j]
        return s[::-1][:m - next_list[n]] + s
