"""

link: https://leetcode.com/problems/reverse-words-in-a-string

problem: 翻转句子中的单词。

solution: split and join

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        in_list = s.split(" ")
        out_list = []
        for x in reversed(in_list):
            if x == "":
                continue
            out_list.append(x)
        return " ".join(out_list)
