"""

link: https://leetcode.com/problems/binary-tree-postorder-traversal

problem: 后序遍历，要求循环不能用递归

solution: 模拟递归的 DFS 栈，加一个标志位判断该节点是否曾被展开

solution-fix: 考虑后序是左右中，等同于实现一个反向的中右左，逆序输出即可

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        class stack_item:
            def __init__(self, node: TreeNode):
                self.node = node
                self.done = False

        s, res = [stack_item(root)], []
        while len(s) != 0:
            t = s.pop()
            if t.done or (not t.node.left and not t.node.right):
                res.append(t.node.val)
            else:
                t.done = True
                s.append(t)
                if t.node.right:
                    s.append(stack_item(t.node.right))
                if t.node.left:
                    s.append(stack_item(t.node.left))
        return res

# ---
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        s, res = [root], []
        while len(s) != 0:
            t = s.pop()
            res.append(t.val)
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        return res[::-1]
