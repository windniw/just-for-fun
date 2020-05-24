"""

link: https://leetcode.com/problems/remove-k-digits

problem: 对数字num挪掉k位，问所有移除方式中的最大值

solution: 栈。扫一遍维护一个非严格递增序列，当发生降序时出栈挪掉高位数字。

"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s, i = [], 0
        while k and i < len(num):
            x = num[i]
            if not s or s[-1] <= x:
                s.append(x)
                i += 1
                continue
            s.pop()
            k -= 1
        s.extend(num[i:])
        s = s[:len(s) - k]
        return "".join(s).lstrip('0') or '0'
