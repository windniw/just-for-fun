"""

link: https://leetcode-cn.com/problems/remove-invalid-parentheses

problem: 从给定字符串中删除最少的 '(' 或 ')' 字符，使字符串的括号合法，求所有的输出可能，注意，字符串中不止包括括号字符

solution: BFS。暴力搜索，对字符串中的每个括号进行移除，判断移除结果中是否有合法序列，若有，直接返回，此时必定为删除数最少，若没有，重复此过程。

"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(x: str) -> bool:
            cnt = 0
            for k in x:
                if k == '(':
                    cnt += 1
                elif k == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        q = {s}
        while q:
            ns, ss = list(filter(valid, q)), set()
            if ns:
                return ns
            for x in q:
                for i, k in enumerate(x):
                    if k == '(' or k == ')':
                        ss.add(x[:i] + x[i + 1:])
            q = ss
        return ['']
