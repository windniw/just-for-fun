"""

link: https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies

problem: 给 n 个任务，他们属于 m 个分组或不属于任何分组，任务间存在依赖关系，且要求同组的任务必须连续完成，求可能的完成顺序

solution: 按所在组对任务进行分组，对组做拓扑序，再对组内做拓扑序

"""
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        in_to, out_to = collections.defaultdict(set), collections.defaultdict(set)
        in_deg, out_deg = [0 for _ in range(n)], [0 for _ in range(m + n)]
        v_group = [[] for _ in range(m + n)]

        for i, g in enumerate(group):
            if g == -1:
                g = m + i
            v_group[g].append(i)
            group[i] = g

        for i, next_list in enumerate(beforeItems):
            gi = group[i]
            for j in next_list:
                gj = group[j]
                if gi == gj:
                    in_to[j].add(i)
                    in_deg[i] += 1
                else:
                    if gi not in out_to[gj]:
                        out_to[gj].add(gi)
                        out_deg[gi] += 1


        res = []

        def topo_sort(items, deg, to, in_group) -> bool:
            q, cnt = [], 0
            for i in items:
                if deg[i] == 0:
                    q.append(i)

            while q:
                k = q.pop()
                cnt += 1
                if in_group:
                    res.append(k)
                else:
                    if not topo_sort(v_group[k], in_deg, in_to, True):
                        return False

                for t in to[k]:
                    deg[t] -= 1
                    if deg[t] == 0:
                        q.append(t)
            return cnt == len(items)

        return res if topo_sort(range(n + m), out_deg, out_to, False) else []