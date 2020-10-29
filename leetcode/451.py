"""

link: https://leetcode-cn.com/problems/sort-characters-by-frequency

problem: 将字符串按字符出现次数重排序

solution: 桶排。字符总数没几个，计数桶排重输出。

"""

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = [0] * 256
        for w in s:
            cnt[ord(w)] += 1
        t, res = [(cnt[i], chr(i)) for i in range(256)], ""
        t.sort(reverse=True)
        for k in t:
            res += k[1] * k[0]
        return res
