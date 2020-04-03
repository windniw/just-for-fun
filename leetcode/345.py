"""

link: https://leetcode.com/problems/reverse-vowels-of-a-string

problem: 翻转字符串中的元音字符，包括大小写

solution: 双指针扫，先转数组方便交换速度更快

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r, w, n, ss = 0, len(s) - 1, {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}, len(s), list(s)
        while l < r:
            while l < n and ss[l] not in w:
                l += 1
            while r >= 0 and ss[r] not in w :
                r -= 1
            if 0 <= l < r < n:
                # s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r + 1:]
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
        return "".join(ss)
