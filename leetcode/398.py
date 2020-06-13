"""

link: https://leetcode-cn.com/problems/random-pick-index

problem: 离线数组，要求给k随机返回 i，有nums[i] == k

solution: 丢字典维护数组随机返回

solution-fix: 蓄水池抽样。将nums视为数据流，令池大小为1，遍历nums时当 nums[i] == target
              入池模拟数据流动，每次以 1/cnt 保留池子中的下标

"""
class Solution:
    def __init__(self, nums: List[int]):
        self.m = collections.defaultdict(list)
        for i in range(len(nums)):
            self.m[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.m[target])

# ---
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n, cnt, res = len(self.nums), 0, 0
        for i in range(0, n):
            if self.nums[i] == target:
                cnt += 1
                if random.randint(1, cnt) == 1:
                    res = i
        return res

