"""

link: https://leetcode.com/problems/unique-binary-search-trees-ii

problem: 生成所有可能的二叉排序树

solution: DFS + dict 优化

"""

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        m = {}

        def dfs(a, b) -> List[TreeNode]:
            if a > b:
                return [None]
            if (a, b) in m:
                return m[(a, b)]
            res = []
            for x in range(a, b + 1):
                ll = dfs(a, x - 1)
                rl = dfs(x + 1, b)
                for i in ll:
                    for j in rl:
                        t = TreeNode(x)
                        t.left = i
                        t.right = j
                        res.append(t)
            m[(a, b)] = res
            return res

        return [] if n == 0 else dfs(1, n)