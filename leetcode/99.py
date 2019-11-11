"""

link: https://leetcode.com/problems/validate-binary-search-tree

problem: 交换排序树的两个节点，要求原地换回

solution: 先序遍历转换为数组，再扫一遍找到交换点，记录第一个降序位置的前一个值，及最后一个降序位置的后一个值
再交换即可，注意降序点可能有1个（相邻交换），也可能有两个（非相邻交换）

solution-fix: 直接用pre记录前一个值，省略转数组的空间

solution-fix-fix: 题目要求使用O(1)的空间，本质上DFS或者BFS遍历均不满足，可采用莫里斯遍历来达成，类线索树的搞法。
其他思路同上。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        val_list = []

        def dfs(k: TreeNode):
            if not k:
                return
            dfs(k.left)
            val_list.append(k)
            dfs(k.right)

        dfs(root)
        val_list.append(TreeNode(float("inf")))
        a, b = None, None
        for i in range(len(val_list) - 1):
            if val_list[i].val > val_list[i + 1].val:
                if not a:
                    a = val_list[i]
                b = val_list[i + 1]
        a.val, b.val = b.val, a.val

# ---
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        pre = TreeNode(float("-inf"))
        a, b = None, None

        def dfs(k: TreeNode):
            nonlocal a, b, pre
            if not k:
                return
            dfs(k.left)
            if pre.val > k.val:
                if not a:
                    a = pre
                b = k
            pre = k
            dfs(k.right)

        dfs(root)
        a.val, b.val = b.val, a.val