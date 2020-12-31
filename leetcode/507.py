"""

link: https://leetcode-cn.com/problems/perfect-number

problem: 判断正整数 N 是否与其所有除了自身的正因数和相等

solution: 遍历求因数和

"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                res += i + num // i
        return res == num
