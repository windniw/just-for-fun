"""

link: https://leetcode.com/problems/reconstruct-original-digits-from-english

problem: 打乱英文数组s，问其原始的字符串对应的数字

solution: 找规律，构造数字的拓扑序。

"""
class Solution:
    def originalDigits(self, s: str) -> str:
        m, l, res = collections.Counter(s), [0] * 10, ''
        l[0] = m['z']
        l[2] = m['w']
        l[4] = m['u']
        l[6] = m['x']
        l[8] = m['g']
        l[1] = m['o'] - l[0] - l[2] - l[4]
        l[3] = m['t'] - l[2] - l[8]
        l[5] = m['f'] - l[4]
        l[7] = m['v'] - l[5]
        l[9] = m['i'] - l[5] - l[6] - l[8]
        for i in range(10):
            res += str(i) * l[i]
        return res
