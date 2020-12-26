"""

link: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree

problem: 给二叉排序树，求其众数，要求空间O(1)

solution: 中序遍历记录前访问值。

"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res, m, pre, cnt = [], 1, -1, 0

        def dfs(k: TreeNode):
            if not k:
                return
            nonlocal m, res, pre, cnt
            dfs(k.left)
            if k.val == pre:
                cnt += 1
            else:
                pre = k.val
                cnt = 1
            if cnt > m:
                res = [pre]
                m = cnt
            elif m == cnt:
                res.append(pre)
            dfs(k.right)

        dfs(root)
        return res
