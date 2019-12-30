"""

link: https://leetcode.com/problems/second-highest-salary

problem: 子查询 与 offset

"""
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary