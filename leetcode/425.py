"""

link: https://leetcode-cn.com/problems/word-squares

problem: 给定若干字符串，求用其中字符串可以组成的所有单词方块，允许重复使用，定义单词方块为第k行第k列相等的正矩形

solution: dfs + 二分。对原数组去重排序，每轮深搜找前缀的左右端点固定该轮的可选值。

solution: dfs + 字典树。思路同上，不过每轮获取的可选字符串的方式由 排序 + 二分 替换成 构造字典树，每轮获取可选值的时间复杂由 O(logn) 可降到 O(1)

"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return []
        n, m = len(words), len(words[0])
        words = list(set(words))
        words.sort()

        res = []

        def search(cur: [str]):
            i, prefix = len(cur), ""
            if i == m:
                res.append(cur)
                return
            for w in cur:
                prefix += w[i]
            l, r = bisect.bisect_left(words, prefix + 'a' * (m - i)), bisect.bisect_right(words, prefix + 'z' * (m - i))
            for j in range(l, r):
                search(cur + [words[j]])

        search([])
        return res

# ---
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return []
        n, m, tree = len(words), len(words[0]), {'@': []}

        def add(word: str):
            k = tree
            for w in word:
                if w not in k:
                    k[w] = {'@': []}
                k['@'].append(word)
                k = k[w]

        def get(prefix: str) -> [str]:
            k = tree
            for w in prefix:
                if w not in k:
                    return []
                k = k[w]
            return k['@']

        words = list(set(words))
        for word in words:
            add(word)

        res = []

        def search(cur: [str]):
            i, prefix = len(cur), ""
            if i == m:
                res.append(cur)
                return
            for w in cur:
                prefix += w[i]
            for word in get(prefix):
                search(cur + [word])

        search([])
        return res
