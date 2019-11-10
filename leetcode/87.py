"""

link: https://leetcode.com/problems/scramble-string

problem: 将字符串从任意位置断开并选择性翻转得到两个子串，并继续对子串做相同操作
问s1能否通过此操作得到s2。注意，得到子串后，不可以对原串重新划分。

solution: DP。定义 f[k][p1][p2] 为长度为k的两个子串, s1[p1:p1+k]能否通过此操作得到
s2[p2:p2+k]。
显然，基础状态为k==1时，s1[p1] 是否等于 s2[p2]。
递推式为 f[k][p1][p2] = f[i][p1][p2] && f[k-i][p1+i][p2+i]    // 不翻转子串情况
                    || f[i][p1][p2+k-i] && f[k-i][p1+i][p2]  // 翻转子串情况
其中 i ∈ [1,k)
"""

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if len(s1) == 0:
            return True
        l = len(s1)
        f = [[[False for _ in range(l + 1)] for _ in range(l + 1)] for _ in range(l + 1)]
        for k in range(1, l + 1):
            for p1 in range(l - k + 1):
                for p2 in range(l - k + 1):
                    if k == 1:
                        f[k][p1][p2] = s1[p1] == s2[p2]
                        continue
                    for i in range(1, k):
                        f[k][p1][p2] |= (f[i][p1][p2] and f[k - i][p1 + i][p2 + i]) or (
                                f[i][p1][p2 + k - i] and f[k - i][p1 + i][p2])
        return f[l][0][0]