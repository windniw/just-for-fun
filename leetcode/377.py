"""

link: https://leetcode.com/problems/combination-sum-iv

problem: 用数组中数字排成序列，使其和为 target，求排列数总和

solution: 记忆化搜索。

"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(maxsize=None)
        def f(k: int) -> int:
            if not k:
                return 1
            res = 0
            for x in nums:
                if k < x:
                    break
                res += f(k - x)
            return res

        nums.sort()
        return f(target)
