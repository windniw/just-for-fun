"""

link: https://leetcode-cn.com/problems/generalized-abbreviation

problem: 输出字符串的所有缩写，缩写规则为将连续n位用字符串n替代，不可以连续替换

solution: dfs + 备忘录。记录上一操作是否转换了数字。

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
