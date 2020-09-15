"""

link: https://leetcode-cn.com/problems/reconstruct-itinerary

problem: 给有向图和起点，求字典序最小的欧拉通路，保证解存在

solution: Hierholzer 算法。从起点开始做dfs，搜索的同时删除每次跳转的边，搜完的节点入栈，搜索遍历顺序的逆序即为结果。

"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = collections.defaultdict(list)
        for x in tickets:
            m[x[0]].append(x[1])
        for x in m:
            m[x].sort()

        res = []

        def dfs(k: str):
            for i, t in enumerate(m[k]):
                if m[k][i] == "x":
                    continue
                m[k][i] = "x"
                dfs(t)
            res.append(k)

        dfs("JFK")
        res.reverse()
        return res
