"""

link: https://leetcode-cn.com/problems/sort-transformed-array

problem: 给 a, b, c 与升序数组nums，求nums中每个数x的 a*x*x + b*x + c 的升序结果，要求时间复杂度为 O(n)

solution: 二次函数极值点为 -b / (2 * a)，二分找到极点后向两侧扩展，注意 a == 0 时会退化成 1 次函数

"""
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        mid, res, n = -b / (2 * a) if a != 0 else float("-inf"), [], len(nums)
        p = bisect.bisect(nums, mid)
        i, j = p - 1, p
        while i >= 0 and j < n:
            if mid - nums[i] <= nums[j] - mid:
                res.append(a * nums[i] * nums[i] + b * nums[i] + c)
                i -= 1
            else:
                res.append(a * nums[j] * nums[j] + b * nums[j] + c)
                j += 1
        while i >= 0:
            res.append(a * nums[i] * nums[i] + b * nums[i] + c)
            i -= 1
        while j < n:
            res.append(a * nums[j] * nums[j] + b * nums[j] + c)
            j += 1
        return res if (a > 0 or a == 0 and b > 0) else res[::-1]
