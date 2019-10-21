"""

link: https://leetcode.com/problems/largest-rectangle-in-histogram

problem: 给定非负数组，每项代表矩形的高，求该图最大矩形面积

solution: 从左往右扫，若递增则入栈，否则出栈直至递增，这样满足栈中每一项元素，若以该项为高的
最大矩形宽度为stack[k-1] ~ stack[k+1]

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        s, res = [0], 0
        for i in range(1, len(heights)):
            while len(s) != 0 and heights[s[-1]] > heights[i]:
                k = s.pop()
                res = max(res, heights[k] * (i - s[-1] - 1))
            s.append(i)
        return res