"""

link: https://leetcode-cn.com/problems/design-snake-game

problem: 模拟贪吃蛇游戏。

solution: 模拟。双端队列 + 哈希表，维护当前贪吃蛇所占的位置。

"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.foods = food
        self.score = 0
        self.w = width
        self.h = height
        self.body = collections.deque()
        self.body.append((0, 0))
        self.visit = set()
        self.visit.add((0, 0))

    def move(self, direction: str) -> int:
        m = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }
        ii, jj = m[direction]
        next_p = (self.body[-1][0] + ii, self.body[-1][1] + jj)
        if (not (0 <= next_p[0] < self.h and 0 <= next_p[1] < self.w)) or (
                next_p != tuple(self.body[0]) and next_p in self.visit):
            return -1
        self.body.append(next_p)
        self.visit.add(next_p)
        if self.score < len(self.foods) and next_p == tuple(self.foods[self.score]):
            self.score += 1
        else:
            if next_p != self.body[0]:
                self.visit.remove(self.body[0])
            self.body.popleft()
        return self.score
