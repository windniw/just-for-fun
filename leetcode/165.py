"""

link: https://leetcode.com/problems/compare-version-numbers

problem: 版本比较, semver 语法

solution: split完转数字比

"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split("."), version2.split(".")
        i = 0
        while not (i >= len(l1) and i >= len(l2)):
            i1 = l1[i] if i < len(l1) else 0
            i2 = l2[i] if i < len(l2) else 0
            if int(i1) < int(i2):
                return -1
            elif int(i1) > int(i2):
                return 1
            i += 1
        return 0
