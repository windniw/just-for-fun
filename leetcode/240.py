"""

link: https://leetcode.com/problems/search-a-2d-matrix-ii

problem: 矩阵matrix满足 matrix[i][k] < matrix[i][k+1] and matrix[k][i] < matrix[k][i+1]
         求检查target是否存在矩阵中

solution: 从上至下，逐行二分，时间复杂度O(nlogm)

solution-fix: 对矩阵，其右上角数字k满足为一列中的最小值，一行中的最大值；
              若k>target，则当前行不可能存在target，i+=1排除一行；
              若k<target，则当前列不可能存在target，j-=1排除一列；
              逐行逐列缩小即可，时间复杂度O(n+m)

"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def f(list: List[int], k) -> bool:
            l, r = 0, len(list)
            while l <= r:
                mid = (l + r) >> 1
                if list[mid] == k:
                    return True
                elif list[mid] < k:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        if not matrix or not matrix[0]:
            return False
        for x in matrix:
            if x[0] <= target <= x[-1] and f(x, target):
                return True
        return False

#---
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n, m, i, j = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
