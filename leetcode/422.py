"""

link: https://leetcode-cn.com/problems/valid-word-square

problem: 问矩阵是否满足第 k 行与第 k 列完全一致，注意每行字符串可能大于或小于 n

solution: 补全，按左上->右下对角线检查。
"""
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            if len(words[i]) > n:
                return False
            words[i] += 'N' * (n - len(words[i]))
        for i in range(n):
            for j in range(i, n):
                if words[i][j] != words[j][i]:
                    return False
        return True
