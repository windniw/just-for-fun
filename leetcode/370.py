"""

link: https://leetcode-cn.com/problems/range-addition

problem: 给长度为 length 的初始为 0 的数组，做若干次操作，每次增或减一段区间的值，求操作完后的数组结果

solution: 差分。类似差分树的思想，这里不需要动态求区间和，直接用数组更新即可。记原数组为 x, 令 k[0] = x[0], k[1] = x[1] - x[0], ...
          x[i] = x[i] - x[i-1]，称 k 为差分数组。由于区间修改不影响其中间的差值，区间 [i, j] 增加 t 时，差分数组只需要修改 k[i] += t, 
          k[j+1] -= t。最后根据差分数组递推出原数组。

"""
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        k = [0] * length
        for t in updates:
            k[t[0]] += t[2]
            if t[1] != length - 1:
                k[t[1] + 1] -= t[2]
        res = [0] * length
        for i, v in enumerate(k):
            if i == 0:
                res[i] = k[i]
            else:
                res[i] = res[i - 1] + k[i]
        return res
