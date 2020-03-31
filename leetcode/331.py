"""

link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

problem: 验证给定序列是否为一个合法的先序遍历树

solution: 栈模拟遍历过程，合并抛出子树

"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node_list = preorder.split(",")
        s = []
        for x in node_list:
            if x == '#':
                while len(s) > 1 and s[-1] == '#' and s[-2] != '#':
                    s.pop()
                    s.pop()
                s.append('#')
            else:
                s.append(x)
        return s == ['#']
