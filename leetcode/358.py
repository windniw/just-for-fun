"""

link: https://leetcode-cn.com/problems/rearrange-string-k-distance-apart

problem: 重新排列字符串s，问新组成的字符串s'能否满足每个相同字符间至少间隔k-1个元素

solution: 贪心。依次决定s'的每位新字符是什么，放置时优先挑选当前可以放置的（与其之前的相同字符间隔已经有k）且剩余量最大的。
          用堆与队列来实现，先按重复次数入大根堆，每次抛出堆顶元素，放置后将字符入队，当队内元素已经超过k时，证明队首元素可以重新被放置，
          取出重新入堆。

"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        class item:
            def __init__(self, c, n):
                self.n = n
                self.c = c

            def __lt__(self, t):
                return self.n > t.n

            def __str__(self):
                return "c : {}, n: {}".format(self.c, self.n)

            def __repr__(self):
                return "c : {}, n: {}".format(self.c, self.n)

        m, res = collections.Counter(s), ""
        heap, queue = [], collections.deque()
        for c in m:
            heapq.heappush(heap, item(c, m[c]))
        while heap:
            t = heapq.heappop(heap)
            res += t.c
            t.n -= 1
            queue.append(t)
            if len(queue) >= k:
                t = queue.popleft()
                if t.n > 0:
                    heapq.heappush(heap, t)
        return res if len(res) == len(s) else ""
