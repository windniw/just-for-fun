"""

link: https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii

problem: 求二叉排序树中与给定浮点数最接近的k个值，要求在树平衡时，时间复杂度小于O(n)

solution: 滑动窗口。通过中序遍历将二叉排序树转换成升序数组，当窗口的下一个元素比窗口的首元素更接近target时，窗口右移。时间复杂O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        t = []

        def f(k: TreeNode):
            if not k:
                return
            f(k.left)
            t.append(k.val)
            f(k.right)

        f(root)
        i = 0
        while i + k < len(t):
            if math.fabs(t[i + k] - target) < math.fabs(t[i] - target):
                i += 1
            else:
                break
        return t[i:i + k]
