"""

link: https://leetcode.com/problems/unique-paths

problem: 求n*m棋盘从左上角到右下角的路线数，规定每次只能往右或下走一步

solution: DP。dp[0][k] = dp[k][0] = 1; dp[i][j] = dp[i-1][j] + dp[j-1]

solution-fix: 无论怎么走，总的路径一定是由n-1步向下和m-1步向右组成的，转换为，从总共n+m-2步中
挑选任意n-1步来向下走，剩下m-1步默认向右走，即C(n-1,n+m-2)

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(m)]
        for i in range(0, n):
            dp[0] = 1
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[m - 1]

# ---

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2) // math.factorial(n-1) // math.factorial(m-1)