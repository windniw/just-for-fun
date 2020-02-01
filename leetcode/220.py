"""

link: https://leetcode.com/problems/contains-duplicate-iii

problem: 判断是否存在(i,j)，满足 abs(nums[i]-nums[j]) <= t and abs(i-j) <= k

solution: 桶排。压缩数值范围，并只检查相邻的两个桶。

"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        def id_of(x: int) -> int:
            return x // t if t != 0 else x

        m = {}
        for i in range(len(nums)):
            id = id_of(nums[i])
            if id in m:
                return True
            if id - 1 in m and nums[i] - m[id - 1] <= t:
                return True
            if id + 1 in m and m[id + 1] - nums[i] <= t:
                return True
            m[id] = nums[i]
            if i >= k:
                del m[id_of(nums[i - k])]
        return False

