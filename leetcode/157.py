"""

link: https://leetcode-cn.com/problems/read-n-characters-given-read4

problem: 用 read4 实现 read

solution: 循环读。注意放进来的buf已经初始化好了长度，不要用extend，直接指定下标填值就好。

"""
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf: List[str], n: int) -> int:
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        t, w, eof = [' '] * 4, 0, False
        while w < n and not eof:
            r = read4(t)
            if r < 4:
                eof = True
            if w + r <= n:
                buf[w:w+r] = t
                w += r
            else:
                buf[w:n] = t[:n - w]
                w = n
        return w