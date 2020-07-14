"""

link: https://leetcode-cn.com/problems/sliding-window-maximum

problem: 滑动窗口容量为k，求数组每个窗口的最大值

solution: 双端队列。按从大到小的顺序维护窗口内的最大值，记新扫描的值为 x，双端队列中任何小于 x 的值都应该出队，因为窗口是在向
          右移动的，在x左侧，且小于x的值后续不会影响滑动窗口的最大值。注意是小于不是小于等于。

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
