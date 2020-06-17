"""

link: https://leetcode.com/problems/integer-replacement

problem: 给定n，定义一次操作为 n = n // 2 if n is even else n + 1 or n - 1，问至少多少次操作后，n可以为1

solution: 贪心。本质上，操作为消除末位0，当n为偶数时右移，当n为奇数时通过进1或退1将末位置为0；只关注末两位，当其为 11 时的最优操作是
          11 -> 00 -> 0 -> nil，而非 11 -> 10 -> 1 -> 0 -> nil，当且仅当 n 为 3 时特殊情况（这时不是尽可能消0，而是要保留倒数第二位的1）

"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            cnt += 1
            if n == 3:
                return cnt + 1
            elif n & 0b1 == 0:
                n >>= 1
            elif n & 0b10 == 0b10:
                n += 1
            else:
                n -= 1
        return cnt
