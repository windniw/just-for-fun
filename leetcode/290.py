"""

link: https://leetcode.com/problems/word-pattern

problem: 字符串和数组要求判断能否一一映射

solution: 丢map

"""

class Solution:
    def wordPattern(self, pattern: str, strx: str) -> bool:
        m = collections.defaultdict(str)
        mm = collections.defaultdict(str)
        pl = strx.split(' ')
        if len(pattern) != len(pl):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in m and pl[i] not in mm:
                m[pattern[i]] = pl[i]
                mm[pl[i]] = pattern[i]
            elif m[pattern[i]] == pl[i] and mm[pl[i]] == pattern[i]:
                continue
            else:
                return False
        return True
