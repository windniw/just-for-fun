"""

link: https://leetcode-cn.com/problems/palindrome-pairs

problem: 给元素各不相同数组words，求所有满足的 words[i] + words[j] 为回文字符串的元组 (i, j)，且 i != j

solution: 扫一遍构造字典树，将每个元素的逆序在字典树中查找是否存在相同的前缀，注意需处理 i == j 的情况

"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        tree, res = {}, []

        def add(k: dict, x: str, i: int):
            if x == "":
                k['$'] = i
                return
            if x[0] not in k:
                k[x[0]] = {}
            add(k[x[0]], x[1:], i)

        def check(x: str) -> bool:
            n = len(x)
            for i in range(0, n // 2):
                if x[i] != x[n - 1 - i]:
                    return False
            return True

        def collect(k: dict, x: str, i: int):
            nonlocal res
            for w in k:
                if w == '$':
                    if k['$'] != i and check(x):
                        res.append([k['$'], i])
                    continue
                collect(k[w], x + w, i)

        def search(k: dict, x: str, i: int):
            nonlocal res
            if x != "" and '$' in k and check(x):
                res.append([k['$'], i])
            if x == "":
                collect(k, "", i)
                return
            if x[0] in k:
                search(k[x[0]], x[1:], i)

        for i, word in enumerate(words):
            add(tree, word, i)

        for i, word in enumerate(words):
            search(tree, word[::-1], i)

        return res
