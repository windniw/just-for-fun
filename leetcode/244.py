"""

link: https://leetcode-cn.com/problems/shortest-word-distance-ii

problem: 给数组与两个字符串，求两个字符串在数组的最近距离。字符串一定出现在数组中，但可能存在多次。实现类的此查询方法，多次连续调用

solution: 预扫描记录每个单词位置，查询时用双指针求两位置数组的最近元素。

"""
class WordDistance:

    def __init__(self, words: List[str]):
        m = collections.defaultdict(list)
        for i, x in enumerate(words):
            m[x].append(i)
        self.m = m

    def shortest(self, word1: str, word2: str) -> int:
        a, b, i, j = self.m[word1], self.m[word2], 0, 0
        n, m, res = len(a), len(b), abs(a[0] - b[0])
        while i < n and j < m:
            res = min(abs(a[i] - b[j]), res)
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
