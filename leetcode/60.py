"""

link: https://leetcode.com/problems/permutation-sequence

problem: 求n的全排列中，第k大的数

solution: 由高而低，每次挪走 t! 个数

"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num, res = [i + 1 for i in range(n)], ''
        for t in range(n, 0, -1):
            f = math.factorial(t - 1)
            i = (k - 1) // f
            k %= f
            res += str(num[i])
            del (num[i])
        return res