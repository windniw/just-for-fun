"""

link: https://leetcode.com/problems/lexicographical-numbers

problem: 返回 [1, n] 的字典序

solution: str  排序转 int

solution-fix: 递归生成数字。看起来O(n)，实际跑起来还没有直接排序快。

"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        t = [str(i) for i in range(1, n + 1)]
        t.sort()
        return [int(x) for x in t]


# ---
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def f(k: int):
            if k > n:
                return
            res.append(k)
            for x in range(10):
                f(k * 10 + x)

        for i in range(1, 10):
            f(i)
        return res
