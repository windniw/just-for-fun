"""

link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters

problem: 求字符串的最长子串ss，ss满足其中每个字符出现次数均不少于k

solution: 分治。若字符串中每个字符出现次数均大于等于k，则最长子串为本身；否则，那些次数少于k的字符，就会成为子串的分割点。
          递归处理该问题即可，时间复杂度O(nlogn)

"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        m = collections.Counter(s)
        if all([m[x] >= k for x in m]):
            return len(s)
        l, r, res = 0, 0, 0
        while r < len(s):
            if m[s[r]] >= k:
                r += 1
                continue
            res = max(res, self.longestSubstring(s[l:r], k))
            l, r = r + 1, r + 1
        res = max(res, self.longestSubstring(s[l:r], k))
        return res