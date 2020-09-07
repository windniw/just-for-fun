"""

link: https://leetcode-cn.com/problems/generalized-abbreviation

problem: 输出字符串的所有缩写，缩写规则为将连续n位用字符串n替代，不可以连续替换

solution: dfs + 备忘录。记录上一操作是否转换了数字。

solution-fix: 所有缩写可能数量定为 2**n 个，n为原串长度。可以将缩写串表达成长度为 n 的一个二进制数，第 i 为 0 时表示缩写，1 代表不变取原字符。
              更高的时间复杂度，但空间复杂度更好。

"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if word == "":
            return [""]

        @functools.lru_cache(maxsize=None)
        def dfs(k: str, pre_num: bool) -> List[str]:
            if k == "":
                return [""]
            t = []
            for i in range(len(k)):
                for kk in dfs(k[i + 1:], not pre_num):
                    t.append((str(i + 1) + kk) if not pre_num else k[:i + 1] + kk)
            return t

        return dfs(word, False) + dfs(word, True)

# ---
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n, res = len(word), []
        for i in range(1 << n):
            cnt, cur, k, t = 0, 0, i, ""
            while cnt != n:
                if k & 1:
                    cur += 1
                    cnt += 1
                else:
                    if cur != 0:
                        t = str(cur) + t
                    cur = 0
                    t = word[n - 1 - cnt] + t
                    cnt += 1
                k >>= 1
            if cur != 0:
                t = str(cur) + t
            res.append(t)
        return res
