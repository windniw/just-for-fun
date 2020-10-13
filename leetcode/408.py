
"""

link: https://leetcode-cn.com/problems/valid-word-abbreviation

problem: 检查 abbr 是否为 word 的合法缩写

solution: 模拟，注意abbr可能有01情况的数字

"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word += 'a'
        abbr += 'a'
        cnt, i, n = 0, 0, len(word)
        for c in abbr:
            if str.isalpha(c):
                i += cnt
                cnt = 0
                if i >= n or word[i] != c:
                    return False
                i += 1
            else:
                if cnt == 0 and c == '0':
                    return False
                cnt = cnt * 10 + ord(c) - 48
        return i == n
