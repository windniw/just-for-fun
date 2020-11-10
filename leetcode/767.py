"""

link: https://leetcode-cn.com/problems/reorganize-string

problem: 返回任意合法的重排字符串S结果，使得任意相邻字母不同

solution: 若最多字符不超过一半，则有解。以最多字符的个数为桶，按序向每个桶丢入字符即可保证不重复

"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        l, n = [0 for _ in range(26)], len(S)
        for c in S:
            l[ord(c) - 97] += 1
        l = [(l[i], chr(97 + i)) for i in range(26)]
        l.sort(reverse=True)
        if l[0][0] > n // 2 + (n & 1):
            return ""
        buckets, c = [l[0][1]] * l[0][0], 0
        for i in range(1, 26):
            k = l[i]
            m = len(buckets) if k[0] == len(buckets) else len(buckets) - 1
            for j in range(k[0]):
                buckets[c] += k[1]
                c += 1
                c %= m
        res = ""
        for w in buckets:
            res += w
        return res
