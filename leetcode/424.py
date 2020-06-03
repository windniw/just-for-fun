"""

link: https://leetcode.com/problems/longest-repeating-character-replacement

problem: 任意替换字符串的k个字符后，求其最长满足所有元素相同的子串。

solution: 滑动窗口。维护窗口内每个字母的数量，当窗口内出现最多的字母数 
          max(window) <= len(window) - k 时，显然剩余的任何字母都可以被替换

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, cnt = 0, [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('A')] += 1
            if i - l + 1 - max(cnt) > k:
                cnt[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l

