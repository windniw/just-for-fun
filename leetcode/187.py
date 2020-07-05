"""

link: https://leetcode-cn.com/problems/repeated-dna-sequences

problem: 由 ACGT 组成的字符串，求其中重复出现的，长度为10的子串，注意重复子串可重叠

solution: 压缩搜索。将四个字母分别视为 0b00, 0b01, 0b10, 0b11，则长度为 10 的子串可被压缩为一个 20 位的整数进行存储，通过 & mask 即可消除高位，
          用 >> 和 + 来补充低位，压缩完丢集合进行查找，若出现相同的整数，即存在重复子串。

"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def f(x: str):
            if x[0] == 'A': return 0
            if x[0] == 'C': return 1
            if x[0] == 'G': return 2
            if x[0] == 'T': return 3

        if len(s) < 10:
            return []
        m, mask, merge_sum = set(), 0xfffff, f(s[0])
        res = set()
        for i in range(1, len(s)):
            merge_sum = (merge_sum << 2 & mask) + f(s[i])
            if i >= 9:
                if merge_sum in m:
                    res.add(s[i - 9:i + 1])
                m.add(merge_sum)
        return list(res)
