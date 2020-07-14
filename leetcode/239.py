"""

link: https://leetcode-cn.com/problems/sliding-window-maximum

problem: 滑动窗口容量为k，求数组每个窗口的最大值

solution: 双端队列。按从大到小的顺序维护窗口内的最大值，记新扫描的值为 x，双端队列中任何小于 x 的值都应该出队，因为窗口是在向
          右移动的，在x左侧，且小于x的值后续不会影响滑动窗口的最大值。注意是小于不是小于等于。

solution-fix: DP。相对而言是第一种更优，不过提供另一种解决思路。将数据按每k个元素划分为一组，left[i]为组内首元素到i的最大值，
              right[i]为i到组内末元素的最大值，有 max(nums[i:j]) = max(right[i], left[i + k - 1])
              当 i，j 落在同一组时，right[i] == left[i+k-1]，若不同组，分别代表窗口落在两组的最大值

"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = collections.deque(), []
        for i, x in enumerate(nums):
            if i >= k and q[0] == nums[i - k]:
                q.popleft()
            if not q or x > q[0]:
                q.clear()
                q.append(x)
            else:
                while q[-1] < x:
                    q.pop()
                q.append(x)
            if i >= k - 1:
                res.append(q[0])
        return res
# ---
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        for i, x in enumerate(nums):
            if i % k == 0:
                left[i] = x
            else:
                left[i] = max(left[i - 1], x)
        right[n - 1] = nums[n - 1]
        for i in reversed(range(n - 1)):
            if (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])
        res = []
        for i in range(n - k + 1):
            res.append(max(right[i], left[i + k - 1]))
        return res
