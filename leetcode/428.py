"""

link: https://leetcode-cn.com/problems/serialize-and-deserialize-n-ary-tree

problem: 序列化和反序列化n叉树

solution: dfs。用 '#' 代表一次 return。

"""
class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''
        res = ""

        def dfs(k: Node):
            nonlocal res
            res += str(k.val) + ','
            for c in k.children:
                dfs(c)
            res += '#,'

        dfs(root)
        return res[:-1]

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        stack = [Node(0, [])]
        for x in data.split(','):
            if x == '#':
                stack.pop()
                continue
            c = Node(int(x), [])
            stack[-1].children.append(c)
            stack.append(c)
        return stack[0].children[0]
