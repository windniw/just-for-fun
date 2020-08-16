"""

link: https://leetcode-cn.com/problems/flip-game

problem: 将字符串中的++替换成--，求替换一次后可能的结果

solution: 扫一遍。

"""
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] == "+":
                res.append(s[:i] + "--" + s[i + 2:])
        return res