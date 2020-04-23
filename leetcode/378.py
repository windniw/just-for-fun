"""

link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

problem: 矩阵满足每行递增，每列递增，非严格，求矩阵中第k大元素

solution: 二分。平常一维数组二分下标，判断位置中点；而本题二分值区间，判断矩阵中有多少元素大于mid值

"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def cal(k: int) -> int:
            c, res = n - 1, 0
            for x in range(n):
                while c >= 0 and matrix[c][x] > k:
                    c -= 1
                res += c + 1
            return res

        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) >> 1
            t = cal(mid)
            if t >= k:
                r = mid
            else:
                l = mid + 1
        return l
