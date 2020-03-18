"""

link: https://leetcode.com/problems/additive-number

problem: 问能否将一个数组串划分成若干个数字，每个数字为前两个数字之和

solution: 遍历搜索

"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(a: str, b: str, res: str) -> bool:
            if len(a) > 1 and a[0] == "0" or len(b) > 1 and b[0] == "0":
                return False
            if res == "":
                return True
            c = str(int(a) + int(b))
            if len(res) >= len(c) and res[:len(c)] == c:
                return check(b, c, res[len(c):])
            return False

        n = len(num)
        if n < 3:
            return False
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if check(num[:i + 1], num[i + 1:j + 1], num[j + 1:]):
                    return True
        return False