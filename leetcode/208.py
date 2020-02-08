"""

link: https://leetcode.com/problems/implement-trie-prefix-tree

problem: 实现字典树

solution: 每个节点独立成树结构，递归查找

solution-fix: 直接以map形式嵌套存取，补充$为后缀符号标记字符串结束

"""
class Trie:

    def __init__(self):
        self.son = [None for _ in range(26)]
        self.done = False

    def insert(self, word: str) -> None:
        if not word:
            self.done = True
            return
        idx = ord(word[0]) - 97
        if not self.son[idx]:
            self.son[idx] = Trie()
        self.son[idx].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.done
        idx = ord(word[0]) - 97
        return self.son[idx] is not None and self.son[idx].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        idx = ord(prefix[0]) - 97
        return self.son[idx] is not None and self.son[idx].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# ---
class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        word += "$"
        k = self.tree
        for x in word:
            if x not in k:
                k[x] = {}
            k = k[x]

    def search(self, word: str) -> bool:
        word += "$"
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        k = self.tree
        for x in prefix:
            if x not in k:
                return False
            k = k[x]
        return True