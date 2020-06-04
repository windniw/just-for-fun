"""

link: https://leetcode.com/problems/longest-repeating-character-replacement

problem: 任意替换字符串的k个字符后，求其最长满足所有元素相同的子串。

solution: 滑动窗口。维护窗口内每个字母的数量，当窗口内出现最多的字母数 
          max(window) <= len(window) - k 时，显然剩余的任何字母都可以被替换

solution-fix: 滑动窗口。实际上，也不需要知道当前窗口内的最多字母数，只需要知道每次滑动窗口
              右移时，其中最多的字母数可能是多少。注意，这里是可能，而不是确切，因为每次得到
              max_num 实际上是 max(max_num_cur, max_num_history)，但并无所谓，如果
              max_num_cur < max_num_history，得到的长度也不会比之前大，不影响最终结果。

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

# ---
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, cnt, max_num = 0, [0] * 26, 0
        for i, x in enumerate(s):
            cnt[ord(x) - ord('A')] += 1
            max_num = max(max_num, cnt[ord(x) - ord('A')])
            if i - l + 1 - max_num > k:
                cnt[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l
