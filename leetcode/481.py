"""

link: https://leetcode-cn.com/problems/magical-string

problem: 某字符串固定以 122 开头，且仅由 1，2 俩字符组成，且每组 1，2 出现的数量正好可以拼回该字符前序子串，求
         该字符的前 n 位有多少个 1, n ∈ [0,10^5]

solution: 模拟。

"""
class Solution:
    def magicalString(self, n: int) -> int:
        if not n:
            return 0
        f = [0] * (n + 5)
        f[0], f[1], f[2] = 1, 2, 2
        i, j, cnt, c = 2, 3, 1, 1
        while j < n:
            if f[i] == 1:
                f[j] = c
                j += 1
            else:
                f[j], f[j + 1] = c, c
                j += 2
            if c == 1:
                cnt += f[i]
                if j > n:
                    cnt -= j - n
            c = 3 - c
            i += 1
        return cnt
