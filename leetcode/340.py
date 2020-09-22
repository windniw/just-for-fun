"""

link: https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters

problem: 求字符串s中最长最多包含k种字符的子串长度

solution: 双指针滑动窗口。

"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        i, n, m, res = 0, len(s), {}, 0
        for j in range(n):
            m[s[j]] = m[s[j]] + 1 if s[j] in m else 1
            while len(m) > k:
                if m[s[i]] == 1:
                    del (m[s[i]])
                else:
                    m[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
