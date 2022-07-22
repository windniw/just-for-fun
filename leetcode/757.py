"""

link: https://leetcode.cn/problems/set-intersection-size-at-least-two

problem: 给 n 个连续区间，求最小的集合 S，满足 S 中元素与每个区间至少交集为 2

solution: 贪心。区间按末值正序，显然对第一个区间，最优解为取其末尾两个元素，之后可以分为三种情况讨论

          1  a . b                      a  b  | S += 2 (add new a, b)
                    c - d   ==>  c . . d-1 d
          2  a . b               a         b  | S += 1 (add new b)
                 c - d      ==>  c . . . . d
          3  a . . . b                  a  b  | S += 1 (add new a)
                 c - d      ==>  c . . d-1 d
          
          这里注意第三种情况，当新区间的 d 与 b 重合时，新元素不可以直接取 b, d，元素会重合

"""
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        cnt, a, b = 0, -1, -1
        for i in intervals:
            if b < i[0]:
                cnt += 2
                a, b = i[1] - 1, i[1]
            elif a < i[0]:
                cnt += 1
                if b != i[1]:
                    a, b = b, i[1]
                else:
                    a, b = i[1] - 1, b
        return cnt
