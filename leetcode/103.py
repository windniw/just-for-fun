"""

link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

problem: 按深度锯齿输出树的值

solution: BFS遍历树

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        rList, tmp, res, rev = [root], [], [], False
        while len(rList) != 0:
            cur = []
            for k in rList:
                cur.append(k.val)
                if k.left:
                    tmp.append(k.left)
                if k.right:
                    tmp.append(k.right)
            if rev: cur.reverse()
            res.append(cur)
            rList = tmp
            tmp = []
            rev = not rev
        return res