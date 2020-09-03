"""

link: https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters

problem: 移除所有重复字符得到一个子序列，求所有可能的最小字典序结果

solution: 单调栈。记录每个字符的最后位置，从前向后扫，若入栈元素c已在栈中，直接忽略；如果栈顶元素大于c，且栈顶元素在后面还会再次出现，将其出栈。

"""
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        m, stack, visit = {c: i for i, c in enumerate(text)}, [], set()

        for i, c in enumerate(text):
            if c in visit:
                continue
            if not stack or stack[-1] < c:
                stack.append(c)
            else:
                while stack and stack[-1] > c and m[stack[-1]] > i:
                    visit.remove(stack.pop())
                stack.append(c)
            visit.add(c)
        return "".join(stack)
