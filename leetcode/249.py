"""

link: https://leetcode-cn.com/problems/group-shifted-strings

problem: 如果字符串 a 的每个字符轮转k位后变为 b，称 a 可移位为 b，给字符数组，对可移位的字符串进行分组。

solution: 计算相邻字符间隔重压缩为新的字符串，相同则同一组。

"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for word in strings:
            t = ""
            for i in range(len(word)):
                t += chr(97 + (ord(word[i]) - ord(word[i - 1]) + 26) % 26)
            m[t].append(word)
        return [m[x] for x in m]
