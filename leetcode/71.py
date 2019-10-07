"""

link: https://leetcode.com/problems/simplify-path

problem: 路径简化

solution: 栈模拟

"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item == '.' or item == '':
                pass
            elif item == '..':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(item)
        return '/' + '/'.join(stack)