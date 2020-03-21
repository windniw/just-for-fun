"""

link: https://leetcode.com/problems/power-of-three

problem: 检查数字是否为3的幂

solution: 连续除3

"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n :
            n //= 3
        return n == 1
