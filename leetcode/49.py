"""

link: https://leetcode.com/problems/group-anagrams

problem: 对strs按照字符分组，要求同组的字符串，组成的字符和数量均一致

solution: 字面做法，python的库函数真好使

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
