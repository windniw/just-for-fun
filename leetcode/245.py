"""

link: https://leetcode-cn.com/problems/shortest-word-distance-iii

problem: 给数组与两个字符串，求两个字符串在数组的最近距离。字符串一定存在但可能多次，查询字符串相同时，应指定不同位置。

solution: 扫一次记录查询字符串位置，特殊处理查询字符串相同的情况。

"""
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        a, b, res = -1, -1, len(words)
        for i, x in enumerate(words):
            if x == word1:
                a = i
                if b != -1:
                    res = min(abs(a - b), res)
            if x == word2:
                b = i
                if word1 != word2 and a != -1:
                    res = min(abs(a - b), res)
        return res
