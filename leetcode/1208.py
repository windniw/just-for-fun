"""

link: https://leetcode-cn.com/problems/get-equal-substrings-within-budget

problem: 定义等长字符串 s 每位转换为 t 的消耗为 abs(s[i]-t[i])，给最大消耗量 maxCost，求不超过最大消耗条件下，转换 s，使其与 t 有最长的公共子串，
         求子串长度。

solution: 双指针。

"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res, j, cost = 0, 0, 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost and j < i:
                cost -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            if cost <= maxCost:
                res = max(res, i - j + 1)
        return res
