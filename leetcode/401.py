"""

link: https://leetcode.com/problems/binary-watch

problem: 二进制手表，时钟灯有0/1/2/4/8, 分钟灯有 0/1/2/4/8/16/32，12小时制，问当灯数为n时可能的时间

solution: 范围只有 0-60，枚举每个数字对应的灯数

"""
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def calc(k: num) -> int:
            res = 0
            while k:
                res += k & 0x1
                k >>= 1
            return res

        h, m = collections.defaultdict(list), collections.defaultdict(list)
        for i in range(12):
            h[calc(i)].append(str(i))
        for i in range(59):
            m[calc(i)].append(str(i) if i > 9 else '0' + str(i))

        res = []
        for i in range(num + 1):
            for j1 in h[i]:
                for j2 in m[num - i]:
                    res.append(j1 + ":" + j2)
        return res
