"""

link: https://leetcode-cn.com/problems/optimal-account-balancing

problem: 记a借给b共计x元为一个元组(a,b,x)，给若干元组，问还款时的最少交易次数

solution: 搜索 + 剪枝。预处理每人欠款情况，若还款时需收款为正，付款为负。又因为本题求最少交易次数，对如下场景，A 付款，BC收款
          将 A 拆分分别付给 BC，等价于 A 先全部付给 B，B 再部分付给 C；交易次数均为 2。暴力枚举每一个人将其应付款或应欠款转移
          给其之后的每个人的交易次数。裸搜会超时，做三种剪枝，若 cnt 大于等于当前最优解，放弃本轮搜索；若当前该人应付应收为0，直
          接忽略；若AB均为收款或均为付款人，不转移其债务。分别对应以下的 123 注释。

"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        if not transactions:
            return 0
        n = 0
        for a, b, _ in transactions:
            n = max(a, b, n)

        f = [0 for _ in range(n + 1)]
        for a, b, c in transactions:
            f[a] += c
            f[b] -= c

        res = float("inf")

        def dfs(k, cnt: int):
            nonlocal res
            if cnt >= res:               # 1
                return
            if k > n:
                res = min(res, cnt)
                return
            if f[k] == 0:                # 2
                dfs(k + 1, cnt)
            for i in range(k + 1, n + 1):
                if f[k] * f[i] < 0:      # 3
                    f[i] += f[k]
                    dfs(k + 1, cnt + 1)
                    f[i] -= f[k]

        dfs(0, 0)
        return res
