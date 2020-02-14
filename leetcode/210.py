"""

link: https://leetcode.com/problems/course-schedule-ii

problem: 查找图的拓扑序

solution: BFS遍历

"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ins = [0] * numCourses
        edges = collections.defaultdict(list)
        for x in prerequisites:
            edges[x[1]].append(x[0])
            ins[x[0]] += 1
        work_queue, res = [], []
        for x in range(numCourses):
            if ins[x] == 0:
                work_queue.append(x)
        while work_queue:
            x = work_queue.pop()
            res.append(x)
            for k in edges[x]:
                ins[k] -= 1
                if ins[k] == 0:
                    work_queue.append(k)
        return res if len(res) == numCourses else []
