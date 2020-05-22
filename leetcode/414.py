"""

link: https://leetcode.com/problems/third-maximum-number

problem: 求数组第三大数，要求时间 O(n)

solution: 遍历记录前三值

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1, m2, m3 = float("-inf"), float("-inf"), float("-inf")
        for x in nums:
            if x > m1:
                m1, m2, m3 = x, m1, m2
            elif x == m1:
                continue
            elif x > m2:
                m2, m3 = x, m2
            elif x == m2:
                continue
            elif x > m3:
                m3 = x
        return m1 if m3 == float("-inf") else m3
