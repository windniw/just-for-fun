"""

link: https://leetcode.com/problems/add-binary

problem: 字符串输入，求二进制加法

solution: 转数字加完转回去 

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]