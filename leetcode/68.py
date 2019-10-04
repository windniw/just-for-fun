"""

link: https://leetcode.com/problems/text-justification

problem: 按规则整理输入文本，要求贪心塞字符串，不超过最大行长度情况，
         且支持居中对齐和向左对齐两种能力

solution: 模拟就是了

"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def next_line(k: int) -> (int, [str]):
            l, line = 0, []
            while k < len(words) and l + len(words[k]) <= maxWidth:
                l += len(words[k]) + 1
                line.append(words[k])
                k += 1
            return k, line

        def arrange_line(line: List[str]) -> str:
            if len(line) == 1:
                return line[0] + ' ' * (maxWidth - len(line[0]))
            l = 0
            for k in line: l += len(k)
            res = ""
            each = (maxWidth - l) // (len(line) - 1)
            for i in range(len(line)):
                res += line[i]
                if i != len(line) - 1:
                    res += ' ' * (each + 1) if i < (maxWidth - l) % (len(line) - 1) else ' ' * each
            return res

        def last_line(line: List[str]) -> str:
            res = ""
            for k in line: res += k + ' '
            return (res + ' ' * (maxWidth - len(res)))[:maxWidth]

        cur, res = 0, []
        while cur < len(words):
            cur, line = next_line(cur)
            res.append(arrange_line(line)) if cur != len(words) else res.append(last_line(line))
        return res