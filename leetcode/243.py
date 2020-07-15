"""

link: https://leetcode-cn.com/problems/shortest-word-distance

problem: 给数组与两个字符串，求两个字符串在数组的最近距离。字符串一定出现在数组中，但可能存在多次。

solution: 扫一次记位置。

"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        a, b, res = -1, -1, len(words)
        for i, x in enumerate(words):
            if x == word1:
                a = i
            elif x == word2:
                b = i
            if a != -1 and b != -1:
                res = min(res, abs(a - b))
        return res
