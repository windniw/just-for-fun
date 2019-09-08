"""

link: https://leetcode.com/problems/trapping-rain-water

problem: 求heigh中所有的凹部分与较小边界之差的和

solution: 从左往右扫一遍找出所有的凹部分，再从右往左扫，排掉最右侧的凹部分即可

solution-fix: 时间复杂度还是O(n)，空间复杂度还是O(1)，没有优化，不过思路很好看。
              S(水) = S(从左往右映射) + S(从右往左映射) - S(墙) - S(矩形)，自己画画就理解了
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left, s, res = height[0], 0, 0
        for k in range(1, len(height)):
            if height[k] >= left:
                left = height[k]
                res += s
                s = 0
            else:
                s += left - height[k]

        if s != 0:
            right, s = height[-1], 0
            for k in range(len(height)-2, -1, -1):
                if height[k] >= right:
                    right = height[k]
                    res += s
                    s = 0
                else:
                    s += right - height[k]
                if height[k] >= left:
                    break
        return res

# ---
class Solution:
    def trap(self, height: List[int]) -> int:
        s, wall, left, right = 0, 0, 0, 0
        for k in range(len(height)):
            left = max(left, height[k])
            right = max(right, height[-1-k])
            s += left + right
            wall += height[k]
        return s - wall - left * len(height)
