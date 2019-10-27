"""

link: https://leetcode.com/problems/gray-code

problem: 构造n位格雷码序列，定义格雷码为相邻位有且仅有一位不同的二进制数字

solution: 递归，想象以下构造方式
0 1
00 01 + 11 10
000 001 011 010 + 110 111 101 100

"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = self.grayCode(n - 1)
        return res + [i + (1 << (n-1)) for i in reversed(res)]
