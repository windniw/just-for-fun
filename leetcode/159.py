"""

link: https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters

problem: 求最长子串长度，满足子串内字符种类少于等于2

solution: 双指针扫。

"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = collections.defaultdict(int)
        i, j, res = 0, 0, 0
        while j < len(s):
            m[ord(s[j])] += 1
            j += 1
            while len(m) > 2 and j - i > res:
                m[ord(s[i])] -= 1
                if m[ord(s[i])] == 0:
                    del (m[ord(s[i])])
                i += 1
            if len(m) <= 2:
                res = max(res, j - i)
        return res