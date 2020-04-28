"""

link: https://leetcode.com/problems/decode-string

problem: 定义串的压缩格式为 "3[a]2[bc]" ==> "aaabcbc"，解压缩

solution: 递归构造。

"""
class Solution:
    def decodeString(self, s: str) -> str:
        i, t, n = 0, "", len(s)

        def next_key_num(i: int) -> (int, int):
            t = 0
            while s[i] != '[':
                t = t * 10 + ord(s[i]) - 48
                i += 1
            return i, t

        while i < n:
            if '0' <= s[i] <= '9':
                i, cnt = next_key_num(i)
                ii, ii_t = i, 0
                while True:
                    ii_t += s[ii] == '['
                    ii_t -= s[ii] == ']'
                    if ii_t == 0:
                        break
                    ii += 1
                return t + cnt * self.decodeString(s[i + 1:ii]) + self.decodeString(s[ii + 1:])
            else:
                t += s[i]
            i += 1
        return t
