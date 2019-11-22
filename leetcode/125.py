"""

link: https://leetcode.com/problems/valid-palindrome

problem: 检查回文，只考虑字母及数字

solution: 对称扫

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        i, j = 0, len(s) - 1
        while i < j and i < len(s) and j >= 0:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
