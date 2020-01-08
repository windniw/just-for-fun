"""

link: https://leetcode.com/problems/binary-search-tree-iterator

problem: 遍历二叉树

solution: 先序遍历

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        self.iterator = 0

        def dfs(k: TreeNode):
            if not k:
                return
            dfs(k.left)
            self.data.append(k.val)
            dfs(k.right)

        dfs(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.iterator += 1
        return self.data[self.iterator - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.iterator < len(self.data)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()