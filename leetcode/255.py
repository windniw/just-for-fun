"""

link: https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree

problem: 给数组，验证是否为二叉搜索树的先序遍历，要求空间O(1)

solution: 分离左右子树，递归验证。时间O(n^2)，超时。

solution-fix: 单调栈。扫一遍在栈上建树，每次出现了升序必然出现右子树，出栈所有小于该节点的元素，最后一个出栈的为该右子树的根节点
              更新全局最小值，当某根的右子树出现，后续不可能出现比该根元素还小的节点。

"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if len(preorder) == 0 or len(preorder) == 1:
            return True
        k = len(preorder)
        for i, x in enumerate(preorder):
            if x > preorder[0]:
                k = i
                break
        l, r = preorder[1:k], preorder[k:]
        return (not l or max(l) < preorder[0]) and (not r or preorder[0] < min(r)) and self.verifyPreorder(
            l) and self.verifyPreorder(r)

# ---
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        n, cur_min, stack = len(preorder), float("-inf"), []
        for i, x in enumerate(preorder):
            if x < cur_min:
                return False
            while stack and stack[-1] < x:
                cur_min = stack.pop()
            stack.append(x)
        return True
