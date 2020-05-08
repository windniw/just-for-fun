"""

link: https://leetcode.com/problems/lexicographical-numbers

problem: 返回 [1, n] 的字典序

solution: str  排序转 int

"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        t = [str(i) for i in range(1, n + 1)]
        t.sort()
        return [int(x) for x in t]
