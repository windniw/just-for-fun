"""

link: https://leetcode-cn.com/problems/add-and-search-word-data-structure-design

problem: 实现数据结构，支持 addword 加入一个单词，search 搜索模板串，模板串中 . 可以代表任意单词

solution: 字典树。

"""
class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        word += '$'
        t = self.tree
        for x in word:
            if x not in t:
                t[x] = {}
            t = t[x]

    def search(self, word: str) -> bool:
        word += '$'

        def dfs(k: dict, i: int) -> bool:
            if i >= len(word):
                return True
            if word[i] != '.':
                return dfs(k[word[i]], i + 1) if word[i] in k else False
            else:
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    if x in k and dfs(k[x], i + 1):
                        return True
                return False

        return dfs(self.tree, 0)
