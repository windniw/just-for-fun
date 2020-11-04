"""

link: https://leetcode-cn.com/problems/circular-array-loop/submissions

problem: 定义循环数组中的跳转为 nums[i] --> nums[i + nums[i]]，问数组中是否存在循环跳转，要求跳转次数大于1，且跳转方向相同
         要求时间O(n)，空间O(1)

solution: 模拟。从任一点（记为nums[i]）进行跳转，有三种可能：
          - 以相同方向跳转回到本轮跳转的某一个节点，然后开始循环，若循环路径大于 1，则出现题设现象，返回 True
          - 跳转过程中出现反方向，即 nums[c] 跳转到 nums[k] 时，发现两节点符号相反，此时可知本轮所有跳转，
            即 nums[i] 到 nums[c] 路径的所有节点，无论如何不可能在循环路径上，因为他们的下一跳方向有异，放弃路径的所有节点，开始下一轮
          - 以相同方向跳转到之前某轮访问过的节点，由 2 可知此节点不可能在循环路径上。同样放弃本轮所有节点，开始下一轮。
          每个节点只会被标记一次，时间O(n)，又已知 nums[i] 属于 [-1000, 0) ∪ (0, 1000]，用 1000 以上的数字来在原数组标记每一轮，可节省
          标记数组的空间，使得空间O(1)

"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, cnt = len(nums), 1000
        left, right = True, False
        for i in range(n):
            if nums[i] > 1000:
                continue
            c, k, cnt, l = i, i, cnt + 1, 0
            f = right if nums[i] > 0 else left
            while -1000 <= nums[k] <= 1000:
                if (nums[k] < 0 and f == right) or (nums[k] > 0 and f == left):
                    break
                l += 1
                c = k
                k = ((k + nums[k]) % n + n) % n
                nums[c] = cnt
            if nums[k] == cnt and c != k:
                return True
        return False
