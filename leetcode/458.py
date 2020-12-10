"""

link: https://leetcode-cn.com/problems/poor-pigs

problem: buckets 桶水中有且仅有一桶有毒，问最少使用多少头猪可以在 k 次测试内找到毒桶，k == minutesToTest // minutesToDie

solution: 信息熵。可以这么想，每头猪有 k+1 个状态（活到第k轮测试后，及在最后一轮死亡），即其可以携带的信息为 k+1。将其想象为一个 k+1 进制的编码，对于任意桶，总是可以
          构造一个编码使其对应。则，题目可以转为：对于 x 位的 k+1 进制编码，求一个最小的 x 使得 buckets 在编码范围内。即 (k+1)**x >= buckets。
          则大于等于 log(buckets, k+1) 的最小整数即为所求。

"""
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        state = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets, state))
