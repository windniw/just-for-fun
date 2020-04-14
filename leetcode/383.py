"""

link: https://leetcode.com/problems/ransom-note

problem: 问b字符串是否包括a

solution: 丢进map里统计

"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = collections.defaultdict(int)
        for x in magazine:
            m[x] += 1
        for x in ransomNote:
            if m[x] <= 0:
                return False
            m[x] -= 1
        return True
