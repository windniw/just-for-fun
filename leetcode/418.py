"""

link: https://leetcode-cn.com/problems/sentence-screen-fitting/

problem: 给定行列固定的窗口与若干单词组成的句子，问该句可循环输出几次，同行每个单词间至少应间隔一个空格。

solution: 贪心。直接模拟放，对每行尽可能多放置，特殊处理句子长度和远小于cols的情况。

solution-fix: 查循环节。以每个句子为单元，记录起末的 col 值，当出现循环时直接复用循环节快速统计。

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

# ---
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        for word in sentence:
            if len(word) > cols:
                return 0
        cur_row, cur_col, cnt = 0, 0, 0
        res, visit = [], {}
        while cur_row < rows:
            if cur_col in visit:
                k, sum_row, sum_sen = cur_col, 0, 0
                while not (k == cur_col and sum_row != 0):
                    sum_sen += 1
                    sum_row += visit[k][1]
                    k = visit[k][0]
                cnt += (rows - cur_row - 1) // sum_row * sum_sen
                cur_row += (rows - cur_row -1) // sum_row * sum_row
                while cur_row + visit[cur_col][1] < rows or (
                        cur_row + visit[cur_col][1] == rows and visit[cur_col][0] == 0):
                    cur_row += visit[cur_col][1]
                    cur_col = visit[cur_col][0]
                    cnt += 1
                break
            pre_row, pre_col, half = cur_row, cur_col, False
            for word in sentence:
                if cur_col + len(word) > cols:
                    cur_row += 1
                    cur_col = 0
                if cur_row >= rows:
                    half = True
                    break
                cur_col += len(word) + 1
                if cur_col >= cols:
                    cur_row += 1
                    cur_col = 0
            cnt += 1 if not half else 0
            visit[pre_col] = (cur_col, cur_row - pre_row)
        return cnt
