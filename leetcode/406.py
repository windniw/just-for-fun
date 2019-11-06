"""

link: https://leetcode.com/problems/queue-reconstruction-by-height

problem: 定义(a,b)为，某项值为a，数组中在其之后的元素项，大于等于a的有b个。给一个乱序后的数组，求还原

solution: 排序，按元素值降序，元素值相同时，数量值升序，依序加入新数组res。
当某项A加入时，res的所有元素值均大于等于A[0]，将A放置在满足其A[1]的位置即可。
令A'在A之后加入，则有A'[0] < A[0] || A'[0] == A[0] && A'[1] > A[1]，前者放在A前后，均不影响
后者不可能放在A之后，因为这样不可能同时满足 == A[0] && == A'[0]
以及学习下python这么骚的排序方式。。。
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        res = []
        for k in people:
            res.insert(k[1], k)
        return res