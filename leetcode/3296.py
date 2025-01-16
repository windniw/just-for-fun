"""

link: https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero

problem: 给定一个山的高度，和每个工人的工作时间，求山的高度降到 0 需要的最少时间

tag: medium,try,堆,二分

solution: 最小堆

solution-fix: 二分

"""

import heapq
from typing import List
from math import isqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = []
        for i, k in enumerate(workerTimes):
            heapq.heappush(h, (k, 1, i))
        s, cur_height = 0, 0
        while cur_height < mountainHeight:
            top_item = heapq.heappop(h)
            cur_height += 1 
            (worker_all_time, worker_cnt, worker_idx) = top_item
            worker_cnt += 1
            heapq.heappush(h, (worker_all_time + worker_cnt * workerTimes[worker_idx], worker_cnt, worker_idx))
            s = worker_all_time
        return s

# ---
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(second):
            avaliable_height = 0
            for i in workerTimes:
                avaliable_height += (isqrt(second // i * 8 + 1) - 1) // 2
            return avaliable_height

        max_worker_time = max(workerTimes)
        l, r = 0, int((1+mountainHeight)*mountainHeight//2) * max_worker_time + 1
        res = 0
        while l < r:
            mid = l + (r - l) // 2
            if check(mid) >= mountainHeight:
                res = mid
                r = mid
            else:
                l = mid + 1
        return res