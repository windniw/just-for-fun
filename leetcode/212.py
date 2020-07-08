"""

link: https://leetcode-cn.com/problems/word-search-ii

problem: 给一个字符矩阵和一堆单词，问每个单词能否从矩阵中找到一条路径与单词相同，不允许重复

solution: 字典树 + dfs + 剪枝。用待匹配模板串构造trie，枚举矩阵每个位置为起点，是否在trie中存在相应单词，若找到，则将其从
          trie中移除。

"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0 or len(board) == 0 or len(board[0]) == 0:
            return []
        # build trie
        tree = {}
        for word in words:
            word += '$'
            t = tree
            for x in word:
                if x not in t:
                    t[x] = {}
                t = t[x]

        def has_word(k: dict) -> bool:
            return '$' in k

        n, m, res = len(board), len(board[0]), []

        def dfs(k: dict, i: int, j: int, cur_word: str) -> bool:
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            match, w = False, board[i][j]
            if w in k:
                # 单词匹配
                if has_word(k[w]):
                    res.append(cur_word + w)
                    # 该节点只有 $ 子节点时，移除单词最后一个字符对应的节点，停止递归，并向上检查是否可移除上一个字符
                    if len(k[w]) == 1:
                        k.pop(w)
                        return True
                    else:
                    # 仅移除单词
                        k[w].pop('$')
                board[i][j] = '*'

                for (ii, jj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if dfs(k[w], i + ii, j + jj, cur_word + w) and len(k[w]) == 0:
                        # 若k[w]执行了移除操作，且其已没有其他子节点，移除 k[w]，直接剪枝
                        k.pop(w)
                        board[i][j] = w
                        return True

                board[i][j] = w
            return False

        for i in range(n):
            for j in range(m):
                dfs(tree, i, j, "")
        return res
