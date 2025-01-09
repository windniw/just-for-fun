'''

link: https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i

problem: 求输入1有多少子串满足条件: 重排后可以将输入2作为前缀

solution: 双指针窗口检查

solution-fix: 用 miss_match 计数统一计算有多少个字母还缺省, 节省每次遍历两个map的开销

'''

from collections import defaultdict

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        word2_map = defaultdict(int)
        for c in word2:
            word2_map[c] += 1
        word1_map = defaultdict(int)
        res = 0
        i, j = 0, 0

        def check_valid() -> bool:
            for cc in word2_map:
                if word1_map[cc] < word2_map[cc]:
                    return False
            return True

        while j < len(word1):
            word1_map[word1[j]] += 1
            j += 1
            if check_valid():
                while i < j:
                    res += len(word1) - j + 1
                    word1_map[word1[i]] -= 1
                    i += 1
                    if not check_valid():
                        break
        return res

# ---

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        word2_map = defaultdict(int)
        for c in word2:
            word2_map[c] += 1
        res = 0
        i, j = 0, 0

        miss_match = len(word2_map)

        while j < len(word1):
            c = word1[j]
            if c in word2_map:
                word2_map[c] -= 1
                if word2_map[c] == 0:
                    miss_match -= 1
            j += 1
            if miss_match == 0:
                while i < j and miss_match == 0:
                    res += len(word1) - j + 1
                    c = word1[i]
                    if c in word2_map:
                        word2_map[c] += 1
                        if word2_map[c] == 1 :
                            miss_match += 1
                    i += 1
        return res