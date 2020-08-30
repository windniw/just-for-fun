"""

link: https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal

problem: 对二叉树的垂直分组

solution: BFS。垂直讲起来很复杂，直接看图，对 ABCDEFG 的满二叉树视为如下图，其中 AEF 视为同一列上的点，即第三行只有三列。
          对 root 节点指定坐标为 0，每个左节点的列坐标为父节点的坐标减一，右节点为父节点的坐标加1，按层遍历。

      A
     / \
    /   \
   B     C
  / \   / \ 
 /   \ /   \
D     EF    G

"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        def f(k: TreeNode) -> int:
            if not k:
                return 0
            return max(f(k.left), f(k.right)) + 1

        height = f(root)

        q, qp, res, i, p = [root], [0], [[] for _ in range(2 * height - 1)], 0, height - 1
        while q:
            i += 1
            j, qq, qqp = 0, [], []
            for j, k in enumerate(q):
                pos = qp[j]
                if not k:
                    continue
                res[pos + p].append(k.val)
                if k.left:
                    qq.append(k.left)
                    qqp.append(pos - 1)
                if k.right:
                    qq.append(k.right)
                    qqp.append(pos + 1)
            q = qq
            qp = qqp
        i, j = 0, 2 * height - 2
        while not res[i]:
            i += 1
        while not res[j]:
            j -= 1
        return res[i:j + 1]
