"""

link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii

problem: 自底向上输出树的层次值

solution: BFS

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        s_list, tmp_list = [root], []
        res = []

        while len(s_list) != 0:
            rl = []
            for k in s_list:
                if k.left:
                    tmp_list.append(k.left)
                rl.append(k.val)
                if k.right:
                    tmp_list.append(k.right)
            res.append(rl)
            s_list = tmp_list
            tmp_list = []
        res.reverse()
        return res