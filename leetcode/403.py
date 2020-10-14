"""

link: https://leetcode-cn.com/problems/frog-jump

problem: 用数组表示记录位置i上存在石头，青蛙从0开始，若第i次前进k，则i+1次只能前进 k-1/k/k+1，问其能否到达最后一块石头

solution: DP。dp[i] 记录到第 i 块石头时的前进步数，初始化一个反向查询的map来记录位置v上是否有石头。

"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        m = {v: i for i, v in enumerate(stones)}
        dp = [set() for _ in stones]
        dp[0].add(0)
        for i, cur in enumerate(stones):
            next = set()
            for j in dp[i]:
                next = next.union({j - 1, j, j + 1})
            for step in next:
                if cur + step == stones[-1]:
                    return True
                if cur + step in m:
                    dp[m[cur + step]].add(step)
        return False