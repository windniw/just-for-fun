"""

link: https://leetcode.com/problems/combination-sum-ii

problem: 普通背包

solution: DP直接过的，不过DP还是适合用于只记录背包状态值，拼数组还要做去重比较麻烦，
          用了很暴力的把list排序转tuple，丢进set去重，再转回list的做法

"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        dp[0] = [[]]
        for i in candidates:
            for j in range(target, 0, -1):
                if j - i >= 0:
                    for k in dp[j - i]:
                        t = k.copy()
                        t.append(i)
                        dp[j].append(t)

        def list_to_sort_tuple(l: list) -> tuple:
            l.sort()
            return tuple(l)

        return [list(i) for i in {list_to_sort_tuple(i) for i in dp[target]}]
