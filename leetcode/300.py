"""

link: https://leetcode-cn.com/problems/longest-increasing-subsequence

problem: 求最长上升子序列(LIS)长度

solution: dp。dp[i] 为 nums[:i] 的LIS长度, dp[j] = max{dp[i] + 1 | i < j && nums[i] < nums[j]}。时间复杂度 O(n^2)

solution-fix: dp + 二分。令 tail[i] 为所有长度为 i 的LIS的最后一个元素的最小值。显然 tail 是递增的，否则若有 tail[i] > tail[i+1]，
              LIS[i+1][1:i+1] 可以替换 LIS[i][:i] 的位置，使得tail[i]更短。既然递增，就可以用二分查找。按序扫一次数组，当nums[i]大于
              当前已经记录最长LIS的tail值cur时，直接将nums[i]补在最后面，即 tail[cur+1]=nums[i]；否则，二分查找tail，看nums[i]是否可以
              替换其中的任意一个位置。时间复杂度O(nlogn)

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if nums[i] < nums[j] and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
        return max(dp)

# ---
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tail, cur = [_ for _ in range(n)], -1
        for i in range(n):
            if cur == -1 or nums[i] > tail[cur]:
                cur += 1
                tail[cur] = nums[i]
                continue
            l, r = 0, cur
            while l < r:
                mid = (l + r) >> 1
                if tail[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid
            if tail[l] > nums[i]:
                tail[l] = nums[i]
        return cur + 1