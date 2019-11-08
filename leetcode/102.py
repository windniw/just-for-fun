"""

link: https://leetcode.com/problems/binary-tree-level-order-traversal

problem: 按深度输出树的值

solution: BFS遍历树

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        rList, tmp, res = [root], [], []
        while len(rList) != 0:
            cur = []
            for k in rList:
                cur.append(k.val)
                if k.left:
                    tmp.append(k.left)
                if k.right:
                    tmp.append(k.right)
            res.append(cur)
            rList = tmp
            tmp = []
        return res