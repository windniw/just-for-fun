"""

link: https://leetcode.com/problems/serialize-and-deserialize-bst

problem: 实现二叉排序树的序列化和反序列化操作。

solution: 二叉排序树的先序遍历一定为其升序序列，序列化为后序，两个结合即可确定唯一的树结构。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        return self.serialize(root.left) + " " + self.serialize(root.right) + " " + str(root.val)

    def deserialize(self, data: str) -> TreeNode:
        def f(l: []) -> TreeNode:
            if not l:
                return None
            t = 0
            while l[t] < l[-1]:
                t += 1
            k = TreeNode(l[-1])
            k.left, k.right = f(l[:t]), f(l[t:-1])
            return k

        l = []
        for x in data.split(' '):
            if x != '':
                l.append(int(x))
        return f(l)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))