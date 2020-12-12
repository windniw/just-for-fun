"""

link: https://leetcode-cn.com/problems/super-egg-drop

problem: 有 N 层楼，K 个鸡蛋，已知鸡蛋在高于 F 楼时扔下会摔碎，F ∈ [0, N]，问至少尝试多少轮可以找到 F

solution: DP。反过来想，令 dp[i][j] 为尝试 i 轮，拥有 j 个蛋的情况下，最大可以测试的楼高；注意是最大，所以有
          DP[i][j] = 1 + dp[i-1][j-1] + dp[i-1][j]。即，在DP[i][j]层楼的最优解楼扔下一个鸡蛋k，可能存在两种情况，
          鸡蛋碎了，则剩下的 j-1 个鸡蛋可以用来测试的最大层高为下面的 dp[i-1][j-1] 层；鸡蛋没碎，则剩下的 j 个鸡蛋用来
          测试的最大层高为上面的 dp[i-1][j] 层，再加上一层最优解层。小心 F 的取值为 [0, N]，即 1 轮时最多只能测试 1 层
          而非 2 层

"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 1:
            return 1
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][1] = i
        for i in range(1, K + 1):
            dp[1][i] = 1

        for i in range(2, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
                if dp[i][j] >= N:
                    return i
