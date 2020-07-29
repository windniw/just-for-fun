"""

link: https://leetcode-cn.com/problems/3sum-smaller

problem: 求数组中，和小于 target 的三元组的数量，要求时间O(n^2)

solution: 双指针。O(n^2 * log_n) 的思路很容易想到，排序，枚举i,j后二分找k。将题目简化为，
          求二元组小于target的数量，排序后双指针从左右遍历，时间为O(n)。相似的，排序后，枚举i，双指针确定 j,k的位置，即为 O(n^2)

"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n, res = len(nums), 0
        nums.sort()
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res
