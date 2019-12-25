"""

link: https://leetcode.com/problems/candy

problem: 向数组项分配值，最小从1开始，当某项的权值大于其相邻项时，要求其分配的值也应大于该项, 求最小的分配和

solution: 按权值排序，由低向高分配，当某项为中间的低谷时，分配1，否则大于其相邻的已分配项。时间O(nlogn)，空间O(n)

solution-fix: 双端遍历。先从左往右扫，if rating[i] > rating[i-1] then candy[i] = candy[i-1] + 1，这样在遍历
              完第一次后，candy 满足大于左值的项分配得多；再从右向左扫，类似逻辑，使其满足大于右值的分配多，取max
              时间O(n), 空间O(n)

"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        class child:
            def __init__(self, score, idx):
                self.score = score
                self.idx = idx

        s, candy = [child(ratings[i], i) for i in range(len(ratings))], [_ for _ in range(len(ratings))]
        s.sort(key=lambda x: x.score)
        for x in s:
            left_score, left_candy, right_score, right_candy = float("inf"), 0, float("inf"), 0
            if x.idx != 0:
                left_score, left_candy = ratings[x.idx - 1], candy[x.idx - 1]
            if x.idx != len(ratings) - 1:
                right_score, right_candy = ratings[x.idx + 1], candy[x.idx + 1]

            if x.score <= left_score and x.score <= right_score:
                candy[x.idx] = 1
            elif x.score > left_score and x.score > right_score:
                candy[x.idx] = max(left_candy, right_candy) + 1
            else:
                candy[x.idx] = left_candy + 1 if x.score > left_score else right_candy + 1
        return sum(candy)

# ---
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)


