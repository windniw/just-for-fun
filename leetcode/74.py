"""

link: https://leetcode.com/problems/search-a-2d-matrix

problem: 升序二维数组，问target是否存在

solution: 两次二分，先行后列

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        n, m = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if target <= matrix[mid][0]:
                r = mid
            else:
                l = mid + 1

        if matrix[l][0] == target: return True
        row = l if matrix[l][0] < target else max(l - 1, 0)
        if matrix[row][0] > target: return False

        l, r = 0, m - 1
        while l < r:
            mid = (l + r) >> 1
            if target <= matrix[row][mid]:
                r = mid
            else:
                l = mid + 1
        return matrix[row][l] == target