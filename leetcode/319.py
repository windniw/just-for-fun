"""

link: https://leetcode.com/problems/bulb-switcher

problem: 给n个灯泡，初始全暗，做n次开关翻转，每次间隔n-1个灯泡开关，问最后有几个灯泡是亮的

solution: 对第n个灯泡，若其因数为奇数个，最后就是亮的，反之就是暗的，因为每个灯泡会被开关其因数个数次。
          只有完全平方数的因数会是奇数个，问题转换为n中有几个完全平方数，开方即可。

"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
