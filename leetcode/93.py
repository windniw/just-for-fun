"""

link: https://leetcode.com/problems/restore-ip-addresses

problem: 给定字符串，问所有可能的合法ip集合

solution: DFS

"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def f(ss: str):
            if ss[0] == '0' and len(ss) != 1:
                return False
            if len(ss) == 3:
                return (ord(ss[0]) - 48) * 100 + (ord(ss[1]) - 48) * 10 + ord(ss[2]) - 48 < 256
            return True

        def dfs(s1: str, k: int) -> List[str]:
            if k + 1 > len(s1) or len(s1) > (k + 1) * 3:
                return []
            if k == 0:
                return [s1] if f(s1) else []
            res = []
            for i in range(1, min(4, len(s1))):
                if f(s1[:i]):
                    for j in dfs(s1[i:], k - 1):
                        res.append(s1[:i] + '.' + j)
            return res

        return dfs(s, 3)