"""

link: https://leetcode.com/problems/word-ladder

problem: 给起始单词，结尾单词，与单词列表，问能否每次转换一个字母，使用列表中的单词由起始变换到结尾

solution: 无权最短路图，即BFS。难点在于如何构造图，一个很巧妙的思路，增加虚拟节点。将 hit 的相邻节点记为 hi*, h*t, *it，
          将 hot 的相邻节点记为 ho*, h*t, *ot，这样两个节点就存在了相连路径。构造图后做BFS即可。

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = collections.defaultdict(list)
        wordList.append(beginWord)
        for x in wordList:
            for k in range(len(x)):
                aim = x[:k] + "*" + x[k + 1:]
                d[aim].append(x)
                d[x].append(aim)
        s = {beginWord}
        q = [beginWord]
        res = 0
        while len(q) != 0:
            res += 1
            q2 = []
            for word in q:
                for next_word in d[word]:
                    if next_word == endWord:
                        return (res + 2) // 2
                    if next_word not in s:
                        s.add(next_word)
                        q2.append(next_word)
            q = q2
        return 0
