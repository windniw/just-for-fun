"""

link: https://leetcode.com/problems/h-index

problem: 给定序列，定义 [h] 为 nums 中有 h 个以上的数字值大于等于h，求[h]的最大值

solution: 排序扫一遍

solution-fix: 排序需要 O(nlog)，通过计数排序将时间降到O(n)，对大于n的数字归并到n桶即可

"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        for x in range(len(citations)):
            if citations[x] >= x + 1:
                res = max(x + 1, res)
        return res

# ---
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        data = [0 for _ in range(n + 1)]
        for x in citations:
            data[min(x, n)] += 1
        res, sum = 0, 0
        for x in range(n + 1):
            if n - sum >= x:
                res = max(res, min(n - sum, x))
                sum += data[x]
            else:
                break
        return res
