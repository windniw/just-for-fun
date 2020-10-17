"""

link: https://leetcode-cn.com/problems/sentence-screen-fitting/

problem: 给定行列固定的窗口与若干单词组成的句子，问该句可循环输出几次，同行每个单词间至少应间隔一个空格。

solution: 贪心。直接模拟放，对每行尽可能多放置，特殊处理句子长度和远小于cols的情况。

"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        cur_rows, cur_cols, i, n, cnt = 0, 0, 0, len(sentence), 0
        s = n - 1
        for w in sentence:
            s += len(w)
        while cur_rows < rows:
            if i == 0 and cols - cur_cols >= s:
                t = (cols - cur_cols + 1) // (s + 1)
                cnt += t
                cur_cols += t * (s + 1)
            if cur_cols + len(sentence[i]) > cols:
                cur_rows += 1
                cur_cols = 0
                continue
            cur_cols += len(sentence[i]) + 1
            i += 1
            if i >= n:
                i = 0
                cnt += 1
            if cur_cols > cols:
                cur_rows += 1
                cur_cols = 0
        return cnt
