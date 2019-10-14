"""

link: https://leetcode.com/problems/combinations

problem: 求C(n,k)的值集合

solution: 递归遍历，为防止重复，规定必须递增搜索

solution-fix: 非递归搞法，核心都是按递增序来避免重复。
前者是按字典序 [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
后者是按数字序 [[1,2],[1,3],[2,3],[1,4],[2,4],[3,4]]
即，先用尽量少的数字，如果低位还有+1的空间，就先对低位+1，来获取下一个序列
如果低位加满了，就对高位进一，还原低位，继续处理
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def c(keys: [int], m: int) -> List[List[int]]:
            if m == 1: return [[i] for i in keys]
            t = []
            for i in range(0, len(keys) + 1 - m):
                for sub_res in c(keys[i + 1:], m - 1):
                    t.append([keys[i]] + sub_res)
            return t

        return c(range(1, n + 1), k)

# --- 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp, res = list(range(1, k + 1)) + [n + 1], []

        j = 0
        while j < k:
            res.append(tmp[:k])
            j = 0
            while j < k and tmp[j + 1] == tmp[j] + 1:
                tmp[j] = j + 1
                j += 1
            tmp[j] += 1

        return res
