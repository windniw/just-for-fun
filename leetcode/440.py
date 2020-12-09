"""

link: https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order

problem: 求 [1, n] 的字典序中的第 k 大

solution: dfs。计算每个前缀 prefix 在 [1, n] 中拥有多少个字符串，按字典序从小到大累加前缀字符串数量，当超过 k 时枚举下一位。

"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        m, n_str = len(str(n)), str(n)

        def prefix_nums(prefix: str) -> int:
            cnt, x = 0, len(prefix)
            for i in range(m - x + 1):
                if i == m - x:
                    if prefix == n_str[:x]:
                        cnt += n - int(prefix) * 10 ** i + 1
                        break
                    elif prefix > n_str[:x]:
                        break
                cnt += 10 ** i
            return cnt

        cnt, prefix = 0, ""
        while cnt != k:
            for i in range(10):
                if i == 0 and prefix == "":
                    continue
                c = prefix_nums(prefix + str(i))
                if c + cnt >= k:
                    cnt += 1
                    prefix += str(i)
                    break
                else:
                    cnt += c
        return int(prefix)
