"""

link: https://leetcode-cn.com/problems/license-key-formatting

problem: 格式化字符串，按K位分割

solution: 模拟

"""
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '', -1).upper()
        if not S:
            return ""
        n = len(S)
        res = S[:len(S) % K]
        for i in range(n % K, n, K):
            res += "-" + S[i:i + K]
        return res if res[0] != '-' else res[1:]
