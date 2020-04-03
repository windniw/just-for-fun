"""

link: https://leetcode.com/problems/counting-bits

problem: 统计 [0,n] 每一个数字的1的位数，要求时间O(n)

solution: 观察到每个 [2^(k-1), 2^k] 的数量是 [0, 2^(k-1)-1] 加首位 1 后的结果

"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [_ for _ in range(num + 1)]
        cur, k = 0, 1
        res[0] = 0
        while cur < num:
            for i in range(k):
                cur += 1
                res[cur] = res[i] + 1
                if cur == num:
                    break
            k <<= 1
        return res
