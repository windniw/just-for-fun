"""

link: https://leetcode-cn.com/problems/logger-rate-limiter

problem: 流输入多个消息与其时间戳，若该消息10s内未输出过，则输出，反之忽略

solution: 用 map 记录消息的最近打印时间。

"""
class Logger:

    def __init__(self):
        self.m = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.m or self.m[message] + 10 <= timestamp:
            self.m[message] = timestamp
            return True
        return False
