"""

link: https://leetcode.com/problems/reverse-string

problem: 原地翻转字符串

solution: 遍历交换

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
