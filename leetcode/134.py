"""

link: https://leetcode-cn.com/problems/gas-station

problem: 设存在一条环形路线，线上n个点，给每个点往下个点的消耗，以及每个点的补给量
         问能否从某个点出发，遍历这个环一圈回来

solution: 易得，sum(cost) > sum(gas)时肯定没戏，即可以把问题转换为两个：
          1. 是否有解 <== sum(gas) - sum(total) >= 0
          2. 解在哪个点
          gas      :  1  2  3  4  5
          cost     :  3  4  5  1  2
          -------------------------
          0/current:  0 -2 -4 -1  2
          1/current:  2  0 -2  1  4
          2/current:  4  2  0  3  6
          3/current:  1 -1 -3  0  3
          4/current: -2 -4 -6 -3  0
          手算下，从每个点出发，到达其他点时，当前的油量，可得不管从哪个节点出发
          相邻current的差是不变的，做一个简单的贪心：既然不管从哪个节点开始，
          current最低谷的那个节点都是固定的，那定其终点，也为起点即可，
          通过跑一圈收集补给来把current填成正值。
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, min_res, pos = 0, 0, 0
        for i in range(len(gas)):
            if res < min_res:
                min_res = res
                pos = i
            res += gas[i] - cost[i]
        if res >= 0:
            return pos
        else:
            return -1