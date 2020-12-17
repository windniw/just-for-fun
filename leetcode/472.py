"""

link: https://leetcode-cn.com/problems/concatenated-words

problem: 检查数组中的每一个字符串是否可由数组的两个以上元素拼成，可重复

solution: 记忆化搜索。字典树会超时，需要尽可能压缩状态持久化搜索结果。预先存进集合，dfs 深搜每个前缀子串是否在集合中，存在则递归搜索。

"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words:
            return []
        x = set(words)

        @functools.lru_cache(maxsize=None)
        def dfs(k: str, i: int, pre_exist: bool) -> int:
            if i >= len(k):
                return pre_exist
            if k[i:] in x and pre_exist:
                return True
            for j in range(i + 1, len(k) + 1):
                if k[i:j] in x:
                    if dfs(k, j, i != 0):
                        return True
            return False

        res = []
        for word in words:
            if dfs(word, 0, 0):
                res.append(word)
        return res
