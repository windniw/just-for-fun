"""

link: https://leetcode.com/problems/valid-number

problem: 问字符串是否为合法数字

solution: 只要正则写得好，没有墙角挖不倒

"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lstrip(' ').rstrip(' ')
        r = ['^[+-]?\d+$',  # a
             '^[+-]?\d+\.\d*$', '^[+-]?\d*\.\d+$',  # a.b b.a a. .b
             '^[+-]?\d+\.\d*e[+-]?\d+$', '^[+-]?\d*\.\d+e[+-]?\d+$',  # a.bec a.ec .aec
             '^[+-]?\d+e[+-]?\d+$' # aeb
             ]
        for rr in r:
            if re.match(rr, s) is not None:
                return True
        return False