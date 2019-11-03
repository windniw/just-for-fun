"""

link: https://leetcode.com/problems/validate-binary-search-tree

problem: 验证是否为合法的二叉排序树

solution: 先序遍历完看下是否升序

solution-fix: 用 inf, -inf 定义极大极小，检查每个值是否满足其区间要求

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def f(x: TreeNode) -> List[int]:
            if x is None:
                return []
            t = f(x.left)
            t.append(x.val)
            t.extend(f(x.right))
            return t

        tl = f(root)
        for i in range(1, len(tl)):
            if tl[i] <= tl[i - 1]:
                return False
        return True

# --- 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def f(x: TreeNode, min_n, max_n: float) -> bool:
            if x is None:
                return True
            if not min_n < x.val < max_n:
                return False
            return f(x.left, min_n, x.val) and f(x.right, x.val, max_n)

        return f(root, float("-inf"), float("+inf"))