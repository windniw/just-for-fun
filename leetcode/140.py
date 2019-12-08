"""

link: https://leetcode.com/problems/word-break-ii

problem: 给字符串s，数组list，问s是否能用所有list中的单词组成，无限制次数，输出所有可能

solution: 丢进map加缓存扫

"""

import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        m = {}
        for x in wordDict:
            m[x] = True

        @functools.lru_cache(maxsize=None)
        def dfs(ss: str) -> (bool, List[List[str]]):
            if ss == "":
                return True, [[]]
            res = []
            for i in range(len(ss)):
                if ss[:i + 1] in m:
                    success, sub_res = dfs(ss[i + 1:])
                    if success:
                        for x in sub_res:
                            t = [ss[:i + 1]]
                            t.extend(x)
                            res.append(t)
            return len(res) != 0, res

        _, res = dfs(s)
        r_list = []
        if res != 0:
            for x in res:
                r_list.append(str.join(' ', x))
        return r_list