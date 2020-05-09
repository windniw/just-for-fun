"""

link: https://leetcode.com/problems/utf-8-validation

problem: 判断给定序列是否为合法的 utf-8 编码，要求编码由若干字符组成，每个字符由 1-4 个字节组成。 

solution: 模拟。遍历判断。

"""
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        w = 0
        for x in data:
            if w > 0:
                if (x & 0x80 != 0) and (x & 0x40 == 0):
                    w -= 1
                else:
                    return False
            else:
                w, k = 0, 0x80
                while x & k:
                    w += 1
                    k >>= 1
                if w == 1 or w > 4:
                    return False
                else:
                    w -= 1
        return w <= 0
