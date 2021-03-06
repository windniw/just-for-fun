"""

link: https://leetcode-cn.com/problems/cracking-the-safe

problem: 返回一个最短字符串 s ，使得对任意由 [0, k) 组成的长度为 n 的字符串 ss 均为 s 的子串，其中 k <= 10

solution: 欧拉图。当 n == 1 时，返回一个 0123..k 的字符串为最优解；当 n > 1 时，显然我们希望 s 的每两个相邻子串能有尽量多的公共元素，
          即 s[i:i+n] 与 s[i+1:i+n+1] 各自表示一个 ss，最长的公共元素长度为 n-1。那么，转换问题，将每个由 [0, k) 组成的长度为 n-1 的
          元素作为节点，每个节点有 k 条边，其值分别为k，即用节点与边组成一个子串ss。以 n = 3, k = 2 为例，可构成下图。

                    [0]                    [1]
                        +-----+ 10 +----->
                        |                |
                        v                v
                <----+                   +---->
            [0]  |     00                11    |  [1]
                v---->                   <----v
                        +                +
                        |                |
                        +-----> 01 <-----+
                    [1]                    [0]
          
          对任意构造图，均有该图连通，有 k ** (n-1) 个节点，每个节点出入度均为 k，则该图必然存在欧拉回路。且可注意到，将欧拉回路上的路径串起来，
          即为满足条件的 s，且长度最短（因为每两个相邻的子串共享了 n-1 个元素，不可能更短了），最短的s长度为 k**n + 1。用Hierholzer算法求其欧拉
          回路即可。
          实现上，通过位处理做了优化，使得没必要构造邻接图，将每个节点视为一个 k 进制的长度为 n-1 的数，可将其转换成 10 进制后用连续的数组g来存储。
          同时，在每个节点上用二进制来记录该节点的第k条边是否已访问过，节省存储空间。


"""
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        res, g = "", [0] * (k * k ** n)
        if n == 1:
            for i in range(k):
                res += str(i)
            return res

        def dfs(x: int):
            nonlocal res
            for i in range(k):
                if g[x] & (1 << i) == 0:
                    g[x] |= 1 << i
                    dfs(x % (k ** (n - 2)) * k + i)
                    res += str(i)

        dfs(0)
        return res + "0" * (n - 1)
