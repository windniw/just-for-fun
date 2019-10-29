"""

link: https://leetcode.com/problems/decode-ways

problem: 给定非负数组，用 ord 顺序代表 chr，问有几种可能的组合方式

solution: DP。注意存在字符0，且0不可转换

"""

class Solution:
    def numDecodings(self, s: str) -> int:
        def ff(ss: str):
            return (ord(ss[0]) - 48) * 10 + ord(ss[1]) - 48

        if len(s) == 0: return 0
        f = [0 for _ in range(len(s) + 1)]
        f[-1] = 1
        f[-2] = 1 if s[-1] != '0' else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                if i == 0 or ff(s[i - 1:i + 1]) > 26:
                    return 0
                else:
                    f[i] = 0
            else:
                f[i] = f[i + 1] + f[i + 2] if ff(s[i:i + 2]) <= 26 else f[i + 1]
        return f[0]