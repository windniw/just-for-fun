"""

link: https://leetcode.com/problems/duplicate-emails

problem: 数据查找

"""

SELECT Email FROM Person GROUP BY Email HAVING COUNT(*) > 1