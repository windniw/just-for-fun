"""

link: https://leetcode-cn.com/problems/self-crossing/

problem: 从原点开始，循环上左下右的走 x[i] 的距离，问路径是否相交

solution: 找规律。尝试画图可知，第 i 步有可能与其 i-3, i-4, i-5 的路径相交，逐一检查即可。

"""

class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(3, len(x)):
            if i >= 3 and x[i - 3] >= x[i - 1] and x[i] >= x[i - 2]:
                return True
            if i >= 4 and (x[i - 1] == x[i - 3] and x[2] + x[i - 4] >= x[i - 2]):
                return True
            if i >= 5 and x[i - 2] > x[i - 4] and x[i-1] < x[i-3] and x[i - 1] + x[i - 5] >= x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                return True
        return False
