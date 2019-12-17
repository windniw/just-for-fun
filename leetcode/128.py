"""

link: https://leetcode.com/problems/word-ladder-ii

problem: 给起始单词，结尾单词，与单词列表，问能否每次转换一个字母，使用列表中的单词由起始变换到结尾，
         求所有的最短转换路径。

solution: 构造图后BFS。思路同127，把路径也加入队列里就行。

"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        for x in wordList:
            for k in range(len(x)):
                aim = x[:k] + "*" + x[k + 1:]
                d[aim].append(x)
                d[x].append(aim)
        s = {beginWord}
        q = [[beginWord]]
        while len(q) != 0:
            ss = set()
            q2 = []
            for words in q:
                word = words[-1]
                for next_word in d[word]:
                    if next_word not in s:
                        ss.add(next_word)
                        t = words.copy()
                        t.append(next_word)
                        q2.append(t)
            q = q2
            s = s.union(ss)
            if endWord in s:
                res = []
                for k in q:
                    if k[-1] == endWord:
                        res.append([k[i] for i in range(0, len(k), 2)])
                return res
        return []
