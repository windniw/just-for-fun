"""

link: https://leetcode-cn.com/problems/reverse-words-in-a-string-ii

problem: 翻转单词，单词不变，顺序翻转，要求空间O(1)

solution: 翻转整个字符串，再翻转每个单词

"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        pre = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[pre:i] = s[pre:i][::-1]
                pre = i + 1
        s[pre:len(s)] = s[pre:len(s)][::-1]
