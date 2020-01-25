"""

link: https://leetcode.com/problems/course-schedule

problem: 拓扑序是否成立

solution: BFS队列

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ins = [0] * numCourses
        edges = collections.defaultdict(list)
        for x in prerequisites:
            edges[x[1]].append(x[0])
            ins[x[0]] += 1
        work_queue = []
        for x in range(numCourses):
            if ins[x] == 0:
                work_queue.append(x)
        while work_queue:
            x = work_queue.pop()
            for k in edges[x]:
                ins[k] -= 1
                if ins[k] == 0:
                    work_queue.append(k)
        return sum(ins) == 0
