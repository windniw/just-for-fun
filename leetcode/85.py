"""

link: https://leetcode.com/problems/maximal-rectangle

problem: 给包含字符 "0","1" 的矩形，求只包含 "1" 的最大矩形面积

solution: DP。做如下定义 

height[i][j]: matrix[ i ~ height[i][j] ][j] == 1, 即向上连续"1"的个数
left[i][j]  : height[i][ left[i][j] ~ j ]   >= height[i][j]，即向左高度均不小于当前点的高度的边界值
right[i][j] : height[i][ j ~ right[i][j] ]  >= height[i][j]，即向右高度均不小于当前点的高度的边界值

特别的，当matrix[i][j] == '0'时一定有 height[i][j] == 0, left[i][j] == 0, right[i][j] = m-1,
即高度为0，左右边界均为0（任何一个格子高度不会小于0）

问题转换为如何维护这三个数组

显然有
height[i][j] = height[i][j] + 1 ? matrix[i][j] == '1' : 0
若下一行全部为1时，其边界关系与上一行一致；当下一行有部分为0时，边界值取上行边界于0的极近值，左右类似
left[i][j] = max(left[i-1][j], <pre_zero_pos> + 1) ? matrix[i][j] == '1' : 0
right[i][j] = min(right[i-1][j], <pre_zero_pos> - 1) ? matrix[i][j] == '1' : 0

压缩行状态，转换为一维DP
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        n, m = len(matrix), len(matrix[0])
        height, left, right = [0 for _ in range(m)], [0 for i in range(m)], [m - 1 for i in range(m)]
        res = 0
        for i in range(n):
            for j in range(m):
                height[j] = height[j] + 1 if matrix[i][j] != '0' else 0
            pre = -1
            for j in range(m):
                left[j] = max(left[j], pre + 1) if matrix[i][j] != '0' else 0
                if matrix[i][j] == '0':
                    pre = j
            pre = m
            for j in reversed(range(m)):
                right[j] = min(right[j], pre - 1) if matrix[i][j] != '0' else m - 1
                if matrix[i][j] == '0':
                    pre = j
            for j in range(m):
                res = max(res, (right[j] - left[j] + 1) * height[j])
        return res