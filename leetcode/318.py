"""

link: https://leetcode.com/problems/maximum-product-of-word-lengths

problem: 给字符串数组，求 len(words[i]) * len(words[j]) 的最大值，要求两个字符串不能有重合字母

solution: 位记录预处理

"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def f(s) -> int:
            res = 0
            for x in s:
                res |= 1 << ord(x) - ord('a')
            return res

        n = len(words)
        d = []
        for x in words:
            d.append(f(x))

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not d[i] & d[j]:
                    res = max(res, len(words[i] * len(words[j])))
        return res