"""

link: https://leetcode-cn.com/problems/design-phone-directory

problem: 实现分配与回收数字能力

solution: 两个集合倒换

"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.use = set()
        self.not_use = set(range(maxNumbers))

    def get(self) -> int:
        if not self.not_use:
            return -1
        t = self.not_use.pop()
        self.use.add(t)
        return t

    def check(self, number: int) -> bool:
        return number in self.not_use

    def release(self, number: int) -> None:
        if number in self.use:
            self.use.remove(number)
            self.not_use.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)