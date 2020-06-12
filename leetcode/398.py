"""

link: https://leetcode-cn.com/problems/random-pick-index

problem: 离线数组，要求给k随机返回 i，有nums[i] == k

solution: 丢字典维护数组随机返回。

"""
class Solution:
    def __init__(self, nums: List[int]):
        self.m = collections.defaultdict(list)
        for i in range(len(nums)):
            self.m[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.m[target])
