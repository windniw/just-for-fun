"""

link: https://leetcode.com/problems/employees-earning-more-than-their-managers

problem: 数据查找

"""

SELECT 
    a.Name AS 'Employee'
FROM 
    Employee AS a,
    Employee AS b
WHERE 
    a.Salary > b.Salary 
    AND a.ManagerId = b.Id

---
SELECT a.Name as Employee
FROM Employee a 
LEFT JOIN Employee b ON a.ManagerId = b.Id 
WHERE a.Salary > b.Salary 