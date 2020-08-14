"""

link: https://leetcode-cn.com/problems/unique-word-abbreviation

problem: 判断字符串缩写是否唯一

solution: 转map用set去重

"""
def get_short(x: str) -> str:
    if len(x) < 2:
        return x
    mid = "" if len(x) - 2 <= 0 else str(len(x) - 2)
    return x[0] + mid + x[-1]


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        m = collections.defaultdict(set)
        for x in dictionary:
            m[get_short(x)].add(x)
        self.m = m

    def isUnique(self, word: str) -> bool:
        s = get_short(word)
        return len(self.m[s]) == 0 or (len(self.m[s]) == 1 and word in self.m[s])


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)