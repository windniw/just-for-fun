"""

link: https://leetcode-cn.com/problems/find-leaves-of-binary-tree

problem: 从左向右依次移除树的叶节点，反复直至树为空，按移除顺序返回每轮值

solution: 拓扑排序。将树视为图来处理，记每个子节点向其父节点存在有向边。

solution-fix: 后序遍历。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        m, q, res, = {}, [], []

        def parent(k: TreeNode, p: TreeNode):
            if not k:
                return
            cnt = (k.left is not None) + (k.right is not None)
            m[k] = [p, cnt]
            if cnt == 0:
                q.append(k)
            parent(k.left, k)
            parent(k.right, k)

        parent(root, None)
        while q:
            qq = []
            res.append([x.val for x in q])
            for k in q:
                kp = m[k][0]
                if kp is not None:
                    m[kp][1] -= 1
                    if m[kp][1] == 0:
                        qq.append(kp)
            q = qq
        return res

# ---
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(k: TreeNode) -> int:
            if not k:
                return 0
            l, r = dfs(k.left) + 1, dfs(k.right) + 1
            t = max(l, r)
            if t > len(res):
                res.append([k.val])
            else:
                res[t - 1].append(k.val)
            return t

        dfs(root)
        return res

