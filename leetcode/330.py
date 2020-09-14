"""

link: https://leetcode-cn.com/problems/patching-array

problem: 给非严格升序数组 nums 与范围 n，问至少需要从 [1, n] 中挑选多少数字加入 nums，才可以用 nums 中的数字组成所有 [1, n] 的数

solution: 贪心。记当前已遍历到第 i 个nums元素，已经满足的区间为 [1, cur)
          若 nums[i] <= cur，则向之前每种组合集合加上一个 cur, 满足区间可更新为 [1, nums[i] + cur)；
          若 nums[i] > cur，则当前nums[1:i]无法组成 cur，而 nums[i:] 对组成 cur 没有任何帮助，因为 nums[i:] 每个元素均比 cur 大，
          所以必须补充一个元素来帮助实现 cur；设补充值为 k，补充后满足区间为 [1, k + cur)，显然为了使 [1, k+cur) 能够覆盖 [cur, cur+1),
          k ∈ [1, cur], 更大的 k 对之后的选择没有影响且使得可满足区间更大，贪心选择最大 k 值，即 cur
          证明：反证法。设该贪心算法找到的 k 个值为 x_0, x_1, ... , x_k，若 k 不是最优解，则存在另 l 个数，使得 y_0, y_1, ..., y_l 也能满足条件且l < k；
          按照前提，当第一次失配时 x_1, y_1 ∈ [1, cur)，x_1 = cur, 则 y_1 <= x_1，则引入 y_1 不可能满足 x_2（因为更大的 x_1 也无法覆盖到），所以
          y_2 <= x_2，同理有 y_l <= x_l，而 y_l 不可能满足 x_k ，所以不存在更小的 l 满足 l < k。

"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur, cnt, i = 1, 0, 0
        while cur <= n:
            if i < len(nums) and nums[i] <= cur:
                cur += nums[i]
                i += 1
            else:
                cur = cur + cur
                cnt += 1
        return cnt
