"""

link: https://leetcode.cn/problems/count-integers-with-even-digit-sum/

problem: 求小于 n 的所有正整数中，各位数字和为偶数的数量

solution: 扫一遍直接算

"""

class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            x = i
            cnt = 0
            while x != 0:
                cnt += x % 10
                x //= 10
            if cnt % 2 == 0:
                res += 1
        return res