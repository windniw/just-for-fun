"""

link: https://leetcode-cn.com/problems/read-n-characters-given-read4-ii-call-multiple-times

problem: 用 read4 实现 read，可能有多次读

solution: 注意read4读回来的数据，在本次read中如果没有返回掉，需要存起来不能直接丢弃。

"""
# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:
class Solution:
    def __init__(self):
        self.data = [' '] * 4
        self.data_len = 0

    def read(self, buf: List[str], n: int) -> int:
        t, w, eof = self.data, 0, False
        if self.data_len != 0:
            w = min(self.data_len, n)
            buf[:n] = t[:w]
            self.data_len -= w
            t[:self.data_len] = t[w:w + self.data_len]

        while w < n and not eof:
            r = read4(t)
            if r < 4:
                eof = True
            if w + r <= n:
                buf[w:w + r] = t
                w += r
            else:
                buf[w:n] = t[:n - w]
                t[:w + r - n] = t[n - w:]
                self.data_len = w + r - n
                w = n
        return w