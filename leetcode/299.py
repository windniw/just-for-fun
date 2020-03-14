"""

link: https://leetcode.com/problems/bulls-and-cows

problem: 猜数字，返回有几位数字和位置都猜对，有几位数字对了位置没对

solution: 扫一遍丢map比较

"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s1, s2 = collections.defaultdict(int), collections.defaultdict(int)
        ra, rb = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                ra += 1
            else:
                s1[secret[i]] += 1
                s2[guess[i]] += 1
        for x in s2:
            if s2[x] != 0:
                rb += min(s2[x], s1[x])
        return str(ra) + 'A' + str(rb) + 'B'
