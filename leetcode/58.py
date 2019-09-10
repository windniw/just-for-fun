"""

link: https://leetcode.com/problems/length-of-last-word

problem: 求最后一个词的长度

solution: 切右空格 split 下即可

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.rstrip(' ').split(' ')
        return len(l[-1])
