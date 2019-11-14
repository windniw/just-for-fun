"""

link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

problem: 数组转平衡树

solution: 中间断开，两边递归构造

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums) >> 1
        k = TreeNode(nums[mid])
        k.left = self.sortedArrayToBST(nums[:mid])
        k.right = self.sortedArrayToBST(nums[mid + 1:])
        return k