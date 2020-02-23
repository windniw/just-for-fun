"""

link: https://leetcode.com/problems/majority-element-ii

problem: 求数组中，出现次数超过 len(nums) // 3 的数字，要求时间O(n)，空间O(1)

solution: 摩尔投票法。在基础的摩尔投票法上变形，每次在数组中取走n个不同的数字，如果某数A超过1/n，则最后一定会被留下。
          同时，应注意其逆推理不成立，即使某数最后留下，也并非一定超过 1/n；对最后留下的数字再扫一轮检查其次数。

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candidate_a, cnt_a, candidate_b, cnt_b = -1, 0, -1, 0
        for x in nums:
            if cnt_a == 0 and not (cnt_b != 0 and candidate_b == x):
                candidate_a, cnt_a = x, 1
                continue
            if cnt_b == 0 and not (cnt_a != 0 and candidate_a == x):
                candidate_b, cnt_b = x, 1
                continue

            if candidate_a == x:
                cnt_a += 1
            elif candidate_b == x:
                cnt_b += 1
            else:
                cnt_a -= 1
                cnt_b -= 1
        res = []
        cnt_a, cnt_b = 0, 0
        for x in nums:
            if x == candidate_a:
                cnt_a += 1
            elif x == candidate_b:
                cnt_b += 1
        if cnt_a > len(nums) // 3:
            res.append(candidate_a)
        if cnt_b > len(nums) // 3:
            res.append(candidate_b)
        return res
