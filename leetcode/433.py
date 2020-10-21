"""

link: https://leetcode-cn.com/problems/minimum-genetic-mutation

problem: 给定若干8位字符串的集合，问能否从 start 经过该集合变换得到 end，定义修改且只修改一个字符为一次变换。注意 start 可以不在该
         集合，但 end 不在该集合则无法变换。

solution: BFS。n^2 遍历构建图，转换为图的两点间的最小距离。

"""

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def f(a, b) -> bool:
            cnt = 0
            for i in range(8):
                if a[i] != b[i]:
                    cnt += 1
            return cnt == 1

        bank.append(start)
        bank = list(set(bank))
        m, n = {w: [] for w in bank}, len(bank)
        if end not in m:
            return -1
        for i in range(n - 1):
            for j in range(i, n):
                if f(bank[i], bank[j]):
                    m[bank[i]].append(bank[j])
                    m[bank[j]].append(bank[i])
        q, visit, res = [(start, 0)], set(start), 0
        while q:
            x = q.pop()
            for to in m[x[0]]:
                if to in visit:
                    continue
                if to == end:
                    return x[1] + 1
                visit.add(to)
                q.append((to, x[1] + 1))
        return -1
