"""

link: https://leetcode.com/problems/longest-absolute-file-path

problem: 用字符串表达文件层级结构，求最长的绝对路径

solution: 引入栈，记录每层前缀长度和，当扫描层级小于栈层级时，抛出栈顶元素

"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input += "\n"
        k, n, s, ss = 0, len(input), [], 0

        def next_key() -> (bool, int, int):
            nonlocal k
            is_word, floor, key_len = False, 0, 0
            while k < n and input[k] != '\n':
                if input[k] == '\t':
                    floor += 1
                else:
                    key_len += 1
                if input[k] == '.':
                    is_word = True
                k += 1
            k += 1
            return is_word, key_len, floor

        res = 1
        while k < n:
            is_word, key_len, floor = next_key()
            while len(s) != 0 and s[-1][0] >= floor:
                ss -= s[-1][1] + 1
                s.pop()
            if is_word:
                res = max(res, ss + key_len + 1)
            else:
                s.append((floor, key_len))
                ss += key_len + 1
        return res - 1
