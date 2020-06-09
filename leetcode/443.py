"""

link: https://leetcode.com/problems/string-compression

problem: 压缩字符串，连续相同字符的子串以数字后缀格式压缩

solution: 双指针

"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        k, pre, cnt, n = 0, chars[0], 0, len(chars)

        def put_cnt_in():
            nonlocal k, cnt
            if cnt == 1:
                return
            for x in str(cnt):
                chars[k] = x
                k += 1

        for i in range(n):
            if chars[i] == pre:
                cnt += 1
                continue
            chars[k] = pre
            k += 1
            put_cnt_in()
            pre, cnt = chars[i], 1
        chars[k] = pre
        k += 1
        put_cnt_in()
        return k
