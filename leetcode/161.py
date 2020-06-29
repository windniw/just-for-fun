"""

link: https://leetcode-cn.com/problems/one-edit-distance

problem: 判断两个字符串的编辑距离是否为1，定义一次编辑为增加，删除，替换一个字符，注意不允许替换为相同字符

solution: 拆分为等长和不等长两种检查情况，前者对第一个不同字符均跳过，后者只跳过较长的字符串

solution-fix: 当找到第一个不同字符时，后面可以不用扫了，直接 == 比较就行

"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        if len(s) + 1 < len(t) or s == t:
            return False
        i, j, k = 0, 0, False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if not k:
                    k = True
                    if len(s) == len(t):
                        i += 1
                    j += 1
                    continue
                else:
                    return False
            i += 1
            j += 1
        return True

# ---
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        if len(s) + 1 < len(t):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return s[i + 1:] == t[j + 1:] if len(s) == len(t) else s[i:] == t[j + 1:]
            i += 1
            j += 1
        return s != t
