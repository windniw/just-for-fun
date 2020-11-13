"""

link: https://leetcode-cn.com/problems/matchsticks-to-square

problem: 问给定数组能否精确分成四组，每组的和相等

solution: 搜索。二分再二分。

"""
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        n, m, s = len(nums), [0] * 4, sum(nums)
        avg = s // 4
        if any([k > avg for k in nums]):
            return False
        if s % 4 != 0:
            return False

        def f1(l, a, b, k, i, aim: int) -> bool:
            if a > aim or b > aim:
                return False
            if i >= len(l):
                if a == b:
                    if len(l) != n:
                        return True
                    t1, t2 = [], []
                    for i in range(len(l)):
                        t1.append(l[i]) if k & (1 << i) else t2.append(l[i])
                    return f1(t1, 0, 0, 0, 0, sum(t1) // 2) and f1(t2, 0, 0, 0, 0, sum(t2) // 2)
                else:
                    return False
            if f1(l, a + l[i], b, k | (1 << i), i + 1, aim) or f1(l, a, b + l[i], k, i + 1, aim):
                return True
            return False

        return f1(nums, 0, 0, 0, 0, sum(nums) // 2)