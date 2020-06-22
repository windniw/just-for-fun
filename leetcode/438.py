"""

link: https://leetcode-cn.com/problems/find-all-anagrams-in-a-string

problem: 给小写字母字符串 s, p，求s中所有子串中，p的字母异位词，即组成字符串的字符集一致

solution: 滑动窗口。维护长度为len(p)的窗口内每个字符出现的次数

"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1, c2, res = [0] * 26, [0] * 26, []
        for x in p:
            c2[ord(x) - 97] += 1
        for i, x in enumerate(s):
            c1[ord(x) - 97] += 1
            if i >= len(p):
                c1[ord(s[i - len(p)]) - 97] -= 1
            # debug(c1, c2, sum(c1), sum(c2), i, s[i - len(p) + 1:i + 1])
            if i >= len(p) - 1 and c1 == c2:
                res.append(i - len(p) + 1)
        return res
