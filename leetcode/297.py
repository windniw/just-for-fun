"""

link: https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree

problem: 实现二叉树的序列化与反序列化

solution: 与官方的序列化方式一致，按层序列化，每次读入上一层有效节点数 n 的 2*n 个节点
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        q, out, res = [root], [], ""
        while q:
            qq = []
            for x in q:
                if not x:
                    out.append(None)
                    continue
                out.append(x.val)
                qq.extend([x.left, x.right])
            q = qq if any(qq) else None

        for x in out:
            res += str(x) + ',' if x is not None else 'x,'
        return res[:-1]

    def deserialize(self, data):
        if not data:
            return None
        in_list = data.split(',')
        root = TreeNode(int(in_list[0]))
        q, i = [root], 1
        while i < len(in_list):
            qq = []
            for j in range(len(q)):
                if in_list[i] != 'x':
                    q[j].left = TreeNode(int(in_list[i]))
                    qq.append(q[j].left)
                else:
                    q[j].left = None
                i += 1

                if in_list[i] != 'x':
                    q[j].right = TreeNode(int(in_list[i]))
                    qq.append(q[j].right)
                else:
                    q[j].right = None
                i += 1
            q = qq
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))