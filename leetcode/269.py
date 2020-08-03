"""

link: https://leetcode-cn.com/problems/alien-dictionary

problem: 重定义字母序，给定升序的字符串序列，从其中推定字母间的大小关系，多种可能时输出任意一种，输入非法时返回空

solution: 拓扑排序。比较相邻两个字符串，找到第一个不同的字符，即为大小关系的差异字符，以自小向大为入度构建拓扑求拓扑序。
          注意一种特殊情况，当 abc, ab 时直接判非法。

"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def compare(a: str, b: str) -> tuple:
            n, m, i, j = len(a), len(b), 0, 0
            while i < n and j < m and a[i] == b[j]:
                i += 1
                j += 1
            if i >= n or j >= m:
                return None, n <= m
            return ord(a[i]) - 97, ord(b[j]) - 97

        edge, num, visit, res = [[] for i in range(26)], [0 for _ in range(26)], set(), ""
        for i, word in enumerate(words):
            for x in words[i]:
                visit.add(ord(x) - 97)
            if i == 0:
                continue
            t = compare(words[i - 1], word)
            if t[0] is None:
                if not t[1]:
                    return ""
            else :
                edge[t[0]].append(t[1])
                num[t[1]] += 1
        while True:
            cur, has_next = 0, False
            for x in visit:
                if num[x] == 0:
                    cur, has_next = x, True
                    break
            if has_next:
                num[cur] = -1
                res += chr(cur + 97)
                for k in edge[cur]:
                    num[k] -= 1
            else:
                break

        return res if all([k == 0 or k == -1 for k in num]) else ""
