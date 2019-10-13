"""

link: https://leetcode.com/problems/minimum-window-substring

problem: 求s的子串s'，满足条件s'中包含t的所有字符

solution: 双指针扫，当右指针第一次找到子串时，左指针开始向前直至不满足子串要求，然后继续交替遍历

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0: return ""
        m = collections.defaultdict(int)
        for c in t:
            m[c] += 1

        hasMatch = False

        def match() -> bool:
            nonlocal hasMatch
            if hasMatch:
                return True
            for k in m:
                if m[k] > 0: return False
            hasMatch = True
            return True

        l, r, res, res_l, res_r = 0, 0, len(s) + 1, 0, 0
        while r < len(s):
            if s[r] in m:
                m[s[r]] -= 1
            if match():
                while True:
                    if s[l] not in m:
                        l += 1
                    elif s[l] in m and m[s[l]] < 0:
                        m[s[l]] += 1
                        l += 1
                    else:
                        break
                if r - l + 1 < res:
                    res = r - l + 1
                    res_l = l
                    res_r = r
            r += 1
        return "" if res == len(s) + 1 else s[res_l:res_r + 1]