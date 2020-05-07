"""

link: https://leetcode.com/problems/shuffle-an-array

problem: 随机打乱数组

solution: 循环对 nums[i:] 随机挑一个换到首位

"""
class Solution:

    def __init__(self, nums: List[int]):
        self.raw = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.raw

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        s = self.raw.copy()
        for i in range(len(s)):
            k = random.randint(i, len(s) - 1)
            s[k], s[i] = s[i], s[k]
        return s



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()