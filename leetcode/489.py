"""

link: https://leetcode-cn.com/problems/robot-room-cleaner

problem: 模拟扫地机器人的行为，只通过四个 API 接口情况下遍历整个房间

solution: DFS。首先抛开题目，遍历01矩阵只需要做dfs。本质上这道题是一致的，不过遍历矩阵可以通过栈直接回溯变量，本题多了一个全局的robot，
          在回溯时令robot也回到上一状态即可。

"""
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visit = set()

        def dfs(x, y, direction):
            nonlocal visit
            visit.add((x, y))
            robot.clean()
            for d in range(4):
                if d != 0:
                    robot.turnRight()
                ii, jj = move_list[(direction + d) % 4]
                i, j = x + ii, y + jj
                if (i, j) in visit:
                    continue
                if not robot.move():
                    visit.add((i, j))
                    continue
                dfs(i, j, (direction + d) % 4)
            robot.turnRight()
            go_back()

        dfs(0, 0, 0)
