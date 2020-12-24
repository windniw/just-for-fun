"""

link: https://leetcode-cn.com/problems/keyboard-row

problem: 问给定字符串数组中可以用键盘一行输出的字符串

solution: 遍历检查字符集合。

"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        t = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []
        for word in words:
            w = set(word.lower())
            if not w - t[0] or not w - t[1] or not w - t[2]:
                res.append(word)
        return res
