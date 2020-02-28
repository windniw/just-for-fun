"""

link: https://leetcode.com/problems/single-number-iii

problem: 给定数组中有且仅有两个元素只出现一次，其他均出现两次，求该两个元素，要求时间O(n)，空间O(1)

solution: 位运算。x ^ -x 可以获得最右侧的出现 1 的位。
          记两个数为 a,b，令 mask = a^b，通过 diff = mask & -mask 找到mask的最右的1（其实不一定需要最右，任意一个1位均可）。
          1位代表在该位上 a 与 b 数字相异，一个为0，一个为1，再通过此位筛出nums中该位为1的数字，对其再做一轮异或即可得 a 或 b

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for x in nums:
            mask ^= x
        diff = mask & -mask

        a = 0
        for x in nums:
            if x & diff:
                a ^= x
        return [a, mask ^ a]
