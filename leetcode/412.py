"""

link: https://leetcode.com/problems/fizz-buzz

problem: 模判断

solution: if 遍历

"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            else:
                if i % 3 == 0:
                    res.append("Fizz")
                elif i % 5 == 0:
                    res.append("Buzz")
                else:
                    res.append(str(i))
        return res
