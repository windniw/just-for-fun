"""

link: https://leetcode-cn.com/problems/encode-and-decode-strings

problem: 实现字符串数组的序列化和反序列化

solution: 对每个字符串在前面拼上 长度 + '#' 格式的头

"""
class Codec:
    def encode(self, strs: [str]) -> str:
        res = ""
        for x in strs:
            res += str(len(x)) + '#' + x
        return res

    def decode(self, s: str) -> [str]:
        i, n, res = 0, len(s), []
        while i < n:
            t = 0
            while s[i] != '#':
                t = t * 10 + int(s[i])
                i += 1
            res.append(s[i + 1:i + 1 + t])
            i += 1 + t
        return res
